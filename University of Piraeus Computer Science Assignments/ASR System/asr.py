from __future__ import division 
from scipy.io import wavfile
from scipy import signal
import argparse
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
import librosa
from endpoints import endpoints
import math
from itertools import groupby, count
from preprocess import wav_preprocess, energy_zerocrossings, deviations, detection_params
import more_itertools as mit
from neural_network import *
from statistics import statistics, printDigitConfusionMatrix


Fs = 8000
nfft = 1024
hpforder = 30
lowcut = 100
highcut = 200

NS=30
L = NS*Fs/1000
MS = 10
R = MS*Fs/1000


def word_seperator(audio_wave):
	#print "    [!] Energy calculation.."
	energy, zero_crossings = energy_zerocrossings(audio_wave)
	
	eavg, esig, zcavg, zcsig = deviations(energy,zero_crossings)

	# STEP 7 - Calc Detection Parameters
	_,_, _, _, ITL = detection_params(energy, eavg, esig, zcavg, zcsig)


	count = 0
	silence_range = []
	#print "    [!] Silence calculation.."
	for en in energy:
		count +=1
		if en <= ITL:
			#print count
			silence_range.append(count)
			#print en


	pointss = []
	current_split = []
	current_split.append(silence_range[:1][0])
	#print silence_range
	#for point in silence_range[1:]:
	for pnt in range(1,len(silence_range)):
		fake = True
		point = silence_range[pnt]
		if point - current_split[-1:][0] <= 15:
			current_split.append(point)
		else:
			for i in range(pnt,pnt+8):
				if abs(point - silence_range[i])> 10:
					fake = False
			if fake:
				pointss.append(int(sum(current_split)/len(current_split)))
				del current_split[:]
				current_split.append(point)
			#print "POINT:", point


	words = []

	for i in range(0,len(pointss)-1):
		start_ = pointss[i]
		end_= pointss[i+1]
		start_sample = int((start_-1)*R+1)
		end_sample = int((end_-1)*R+L+1)
		
		words.append(audio_wave[start_sample:end_sample])
	words.append(audio_wave[end_sample:])
	return words


def word_isolator(word_wave):

	energy, zero_crossings = energy_zerocrossings(word_wave)

	totalFrames = len(energy)
	
 	#zero_crossings=zero_crossings*R/(2*L)
	for i in range(0,len(zero_crossings)):
		zero_crossings[i] = zero_crossings[i]*R/(2*L)

	eavg, esig, zcavg, zcsig = deviations(energy,zero_crossings)

	# STEP 7 - Calc Detection Parameters
	IF,IZCT, IMX, ITU, ITL = detection_params(energy, eavg, esig, zcavg, zcsig)

	try:
		B2, E2, B1, E1 = endpoints(energy,zero_crossings,ITU,ITL,IZCT)
		start_sample = int((B2-1)*R+1)
		end_sample = int((E2-1)*R+L+1)
	except:
		start_sample = 0
		end_sample = len(word_wave-1)

	return word_wave[start_sample:end_sample]
		



if __name__ == "__main__":
	
	load_trained_model()

	parser = argparse.ArgumentParser(description='We will see about this text..')
	parser.add_argument("-a","--audio", help="Audio file for ast", required=False)
	parser.add_argument("-f","--folderaudio", help="Folder with audio files for ast", required=False)
	parser.add_argument("-d","--dataset", help="Speaker name for dataset validation", required=False)
	parser.add_argument("-c","--confusion_matrix", help="Print confusion_matrix", required=False)
	args = parser.parse_args()

	if not args.audio and not args.folderaudio:
		print "[X] No audio file found"
		exit()

	
	speaker_name = args.dataset
	if args.folderaudio:
		AUDIO_FOLDER_NAME = args.folderaudio
		wavs = os.listdir(AUDIO_FOLDER_NAME)
		wavs = [x for x in wavs if not x.split("/")[-1].startswith('.')]
		wavs = [x for x in wavs if x.split("/")[-1].endswith('.wav')]
		og_samples = []
		predictions = []
		for wav_file in wavs:
		
			#print ".: Preprocessing phase:."
			audio_wave = wav_preprocess(AUDIO_FOLDER_NAME+"/"+wav_file)
			#librosa.output.write_wav('tediogt.wav', audio_wave, Fs)
			#print "  [!] Seperating words.."
			words =  word_seperator(audio_wave)
			c = 0
			words_isolated_waves = []

			#print "  [!] Isolating words..\n"
			for word in words:
				words_isolated_waves.append(word_isolator(word))

			#print ".:Convolutional Neural Network processing:."
			speech_to_text = []
			for word in words_isolated_waves:
				#librosa.output.write_wav(str(c)+'.wav', word, Fs)
				speech_to_text.append(int(predict_cnn(word)))
				
				c += 1

			# CHANGE THAT
			original=[]
			for n in wav_file.split('.')[0]:
				original.append(int(n))
			print "      File:", wav_file
			print "  Original:", original
			print "Prediction:", speech_to_text, "\n"
			og_samples.append(original)
			predictions.append(speech_to_text)

		stats = statistics(og_samples, predictions)
		printDigitConfusionMatrix(stats)

		#for sample in og_samples: 
		#	print stats['samples'][str(sample)]['confusion_matrix']

	if args.audio:
		AUDIO_FILE_NAME = args.audio
		print ".: Preprocessing phase:."
		audio_wave = wav_preprocess(AUDIO_FILE_NAME)
		#librosa.output.write_wav('tediogt.wav', audio_wave, Fs)
		print "  [!] Seperating words.."
		words =  word_seperator(audio_wave)
		c = 0
		words_isolated_waves = []

		print "  [!] Isolating words..\n"
		for word in words:
			words_isolated_waves.append(word_isolator(word))
	
				
	
		print ".:Convolutional Neural Network processing:."
		speech_to_text = []
		for word in words_isolated_waves:
			#librosa.output.write_wav(str(c)+'.wav', word, Fs)
			speech_to_text.append(int(predict_cnn(word)))
			c += 1

		# CHANGE THAT
		original=[]
		for n in AUDIO_FILE_NAME.split('.')[0]:
			original.append(int(n))
		print "  Original:", original
		print "Prediction:", speech_to_text, "\n"

	if args.dataset:
		corr_data, perc = get_unknown_speaker_acc(speaker_name)
		print corr_data
		print perc, "%"
