from __future__ import print_function
from time import sleep
import math
from random import randint
import argparse
import librosa
from asr import word_seperator, word_isolator
from preprocess import wav_preprocess
import os
from tqdm import tqdm

SPEAKER_NAME = "ll"
DATASET_PATH = "P_DATASET/"
FINAL_DATASET_PATH = 'dataset_cat/'

DELAY_BETWEEN_NUMBERS = 0.1
REPEATS_PER_NUMBER = 1


def create_dir(path):

	def make(dir):
		try:
			os.stat(dir) 
		except:
			os.mkdir(dir) 

	if isinstance(path,str):
		make(path) 
	elif isinstance(path,list):
		make(path[0]) 

		for name in path[1:]:
			make(path[0] + "/" +  str(name))
	else:
		pass	

def set_dataset(path=DATASET_PATH[:-1]):
	
	wavfiles = [path + '/' + wavfile for wavfile in os.listdir(path + '/')]
	wavfiles = [x for x in wavfiles if not x.split("/")[-1].startswith('.')]
	
	for wavfile in tqdm(wavfiles, desc="Moving dataset.."):
		number = wavfile.split("/")[1][0]
		new_file = FINAL_DATASET_PATH + number + "/" + wavfile.split("/")[1]
		os.rename(wavfile, new_file)
			

def generate_number_sequence():
	# We want the numbers jumbled up (helps eliminate any previous-number effects)
	# This function scrambles the numbers in a deterministic way so that we can remember
	# what the order was later.
	# A deterministic shuffle makes labeling easy, makes pausing / resuming the experiment easy, etc.
	nums = [str(i) for i in range(10) for set_num in range(REPEATS_PER_NUMBER)]

	for i in range(len(nums)):
		target = int(round(math.pi * i)) % len(nums)
		(nums[i], nums[target]) = (nums[target], nums[i])

	return nums

def generate_single_number_generate_number_sequence(number):

	return [number]*20


def create_dataset(num_seq):
	#nums = generate_number_sequence()
	nums = generate_single_number_generate_number_sequence(num_seq)
	print("Start Audacity to record the dataset")
	input("Hit enter when ready..")
	print("Starting...")
	sleep(1)

	for i, num in enumerate(nums):
		if (float(i)/len(nums) * 100) % 10 == 0:
			print("\n====", float(i)/len(nums)*100, "% done====\n")
		else:
			print("")

		sleep(DELAY_BETWEEN_NUMBERS/2)
		print(num)
		sleep(DELAY_BETWEEN_NUMBERS/2)

def create_sentence():

	global REPEATS_PER_NUMBER
	num_of_sentences = 2
	print("Start Audacity to record the sentences")
	input("Hit enter when ready..")
	print("Starting...")
	random_len = []
	sentence = []
	sentences = []
	for i in range(0,num_of_sentences):

		REPEATS_PER_NUMBER = randint(4, 10)
		random_len.append(REPEATS_PER_NUMBER)
		nums = generate_number_sequence()
		sleep(1)

		for i, num in enumerate(nums[:REPEATS_PER_NUMBER]):

			sleep(DELAY_BETWEEN_NUMBERS/2)
			print(" ")
			print(num)
			sentence.append(num)
			sleep(DELAY_BETWEEN_NUMBERS/2)

		print("Save as .wav with name: ", end="")
		for nu in sentence:
			print(nu, end="")

		del sentence[:]
		sentences.append(sentence)
		if i == num_of_sentences: exit()
		print("\nSentence ready")
		input("Hit enter for next sentence..")

	return random_len, sentences

if __name__ == '__main__':


	parser = argparse.ArgumentParser(description='Script options..')
	parser.add_argument("-d","--dataset", help="Record dataset objects", action="store_true")
	parser.add_argument("-s","--sentence", help="Record sentences", action="store_true")
	parser.add_argument("-m","--move_dataset", help="Move dataset files", action="store_true")
	args = parser.parse_args()


	

	if  args.dataset:

		create_dir(DATASET_PATH)
		num_seq = int(input("Enter number for sequence: "))
		print("Recoring Dataset..")
		create_dataset(num_seq)

		AUDIO_FILE_NAME = input("audio for datase: ")

		print(".: Preprocessing Dataset:.")
		audio_wave = wav_preprocess(AUDIO_FILE_NAME)
		print("  [!] Seperating words..")
		words =  word_seperator(audio_wave)
		words_isolated_waves = []

		print("  [!] Isolating words..\n")
		for word in words:
			words_isolated_waves.append(word_isolator(word))

		#number_sequence = generate_number_sequence()
		number_sequence =  generate_single_number_generate_number_sequence(num_seq)
		c = 0
		
		number_occ = {
			0:0,
			1:0,
			2:0,
			3:0,
			4:0,
			5:0,
			6:0,
			7:0,
			8:0,
			9:0,

		}
		print("  [!] Saving words to .wav..\n")
		for word in words_isolated_waves:
			librosa.output.write_wav(DATASET_PATH+str(number_sequence[c])+"_"+SPEAKER_NAME+"_"+str(number_occ[int(number_sequence[c])])+'.wav', word, 8000)
			number_occ[int(number_sequence[c])] += 1
			c += 1


	if args.sentence:
		print("Recoring Sentences..")
		create_sentence()

	if args.move_dataset:
		set_dataset()

	if not args.dataset and not args.sentence and not args.move_dataset:
		print("Select an options via args..")



	





