import os
import keras
import numpy as np
import collections
from tqdm import tqdm
import argparse
from collections import defaultdict
from collections import OrderedDict
import librosa, os, glob
import librosa.display
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D,Conv1D,MaxPooling1D
from keras.utils import to_categorical
from keras.callbacks import History
from keras.regularizers import l2
import json,codecs
from preprocess import filter

# Suppress warnings - Needs to be checked.
# ========================================

# OLD FUNCTIONS WARNING 
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)

# CPU WARNING AVX2 FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# ========================================
set_nn_verbosity = 1

speakers_ = ['theo','yweweler','jackson', 'nicolas']
DATA_PATH = 'dataset_cat'

MAX_MFCC_SHAPE = 50
NUMBER_OF_CLASSES = 10
MFCC_NUM = 13
SAMPLING_RATE = 8000

NN_PATH_DATA = 'nn_data'
NN_PATH_DATA_LABELS = NN_PATH_DATA + "/mfcc/"
NN_PATH_DATA_HISTORY = NN_PATH_DATA + "/history/"
audio_data_mfccs = []
path = 'recordings'

validation_speaker = 'theo'
save_model_name = os.path.join(NN_PATH_DATA + "/nn_model/"+validation_speaker+"_model_auto.h5")
count = 0


def get_labels(path=DATA_PATH):
	labels = os.listdir(path)
	labels = [x for x in labels if not x.startswith('.')]
	label_indices = np.arange(0, len(labels))
	#print labels
	return labels, label_indices, keras.utils.to_categorical(label_indices)


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
	



def mfcc_pad(mfcc, max_pad_len=36): # max seen: 36
	#print "minus: ", max_pad_len - mfcc.shape[1]
	
	print "mfcc shape: ", mfcc.shape[1]
	pad_width = max_pad_len - mfcc.shape[1]
	mfcc = np.pad(mfcc, pad_width=((pad_width/4, pad_width/4), (pad_width/4, pad_width/4)), mode='constant')
	
	return mfcc



def wav2mfcc(audio_data, wave_not_wav, max_pad_len=MAX_MFCC_SHAPE):
	
	if not wave_not_wav:
		wave, sr = librosa.load(audio_data, mono=True, sr=None)
		wave = filter(wave,sr)
	else:
		wave = audio_data
		wave = filter(wave,SAMPLING_RATE)
	#wave = wave[::3]



	wave = wave/max(-min(wave), max(wave))

	#S = librosa.feature.melspectrogram(y=wave, sr=SAMPLING_RATE)
	#Slog = 10*np.log10(S)

	D = np.abs(librosa.stft(wave,center=True,pad_mode='constant'))
	Slog = librosa.feature.melspectrogram(S=D)


	#mfcc = librosa.feature.mfcc(wave, sr=SAMPLING_RATE)
	Sdb = librosa.power_to_db(Slog) 
	
	'''
	# Neutralize signal with power (in dB) lower than...
	for i in range(0,len(Sdb)):
		for j in range(0,len(Sdb[0])):
			if Sdb[i][j] < 0:
				Sdb[i][j] = 0
	'''
	mfcc = librosa.feature.mfcc(S=Sdb, n_mfcc = MFCC_NUM)
	#print mfcc.shape


	pad_width = max_pad_len - mfcc.shape[1]
	mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
	return mfcc



def save_data_to_array(path=DATA_PATH, max_pad_len=MAX_MFCC_SHAPE,validation_speaker='theo'):
	labels, _, _ = get_labels(path)

	for label in labels:
		# Init mfcc vectors
		mfcc_vectors = []

		wavfiles = [path + '/' + label + '/' + wavfile for wavfile in os.listdir(path + '/' + label)]
		wavfiles = [x for x in wavfiles if not x.split("/")[-1].startswith('.')]
		#print wavfiles
		wavfiles = [x for x in wavfiles if validation_speaker  not in x]
		for wavfile in tqdm(wavfiles, desc="Acc dataset for: " + label):
			#print wavfile
			#if validation_speaker not in wavfile:
			mfcc = wav2mfcc(wavfile, False, max_pad_len=max_pad_len)
			mfcc_vectors.append(mfcc)
		np.save(NN_PATH_DATA_LABELS + label +'_not_'+validation_speaker+ '.npy', mfcc_vectors)


def save_val_data_to_array(path=DATA_PATH, max_pad_len=MAX_MFCC_SHAPE,validation_speaker='theo'):
	labels, _, _ = get_labels(path)

	for label in labels:
		# Init mfcc vectors
		mfcc_vectors = []

		wavfiles = [path + '/' + label + '/' + wavfile for wavfile in os.listdir(path + '/' + label)]
		wavfiles = [x for x in wavfiles if not x.split("/")[-1].startswith('.')]
		#print wavfiles
		wavfiles = [x for x in wavfiles if validation_speaker in x]
		for wavfile in tqdm(wavfiles, desc="Val dataset for: " + label):
			#print wavfile
			#if validation_speaker in wavfile:
			mfcc = wav2mfcc(wavfile, False, max_pad_len=max_pad_len)
			mfcc_vectors.append(mfcc)
		np.save(NN_PATH_DATA_LABELS + label + '_'+validation_speaker+'.npy', mfcc_vectors)



def get_train_test(split_ratio=0.6, random_state=42):
	# Get available labels
	labels, indices, _ = get_labels(DATA_PATH)

	# Getting first arrays
	X = np.load(NN_PATH_DATA_LABELS + labels[0] +'_not_'+ validation_speaker+ '.npy')
	y = np.zeros(X.shape[0])

	# Append all of the dataset into one single array, same goes for y
	for i, label in enumerate(labels[1:]):
		x = np.load(NN_PATH_DATA_LABELS + label +'_not_'+ validation_speaker + '.npy')
		X = np.vstack((X, x))
		y = np.append(y, np.full(x.shape[0], fill_value= (i + 1)))

	assert X.shape[0] == len(y)

	return X, y
	#return train_test_split(X, y, test_size= (1 - split_ratio), random_state=random_state, shuffle=True)

def get_validation_test(split_ratio=0.6, random_state=42):
	# Get available labels
	labels, indices, _ = get_labels(DATA_PATH)

	# Getting first arrays
	X = np.load(NN_PATH_DATA_LABELS + labels[0] +'_'+validation_speaker+ '.npy')
	y = np.zeros(X.shape[0])

	# Append all of the dataset into one single array, same goes for y
	for i, label in enumerate(labels[1:]):
		x = np.load(NN_PATH_DATA_LABELS + label +'_'+validation_speaker+ '.npy')
		X = np.vstack((X, x))
		y = np.append(y, np.full(x.shape[0], fill_value= (i + 1)))

	assert X.shape[0] == len(y)

	return X, y


def load_trained_model(weights_path=save_model_name):
   #model = create_model()
   model.load_weights(weights_path)

def neural_network_model():
	# ======== MODEL ========
	model = Sequential()

	model.add(Conv1D(32, kernel_size=(2), activation='relu', input_shape=(MFCC_NUM, MAX_MFCC_SHAPE)))
	model.add(MaxPooling1D(pool_size=(2)))
	model.add(Dropout(0.25))
	model.add(Flatten())
	#model.add(Dense(256, kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01), activation='relu'))
	#model.add(Dropout(0.25))
	model.add(Dense(128, kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01), activation='relu'))
	model.add(Dropout(0.25))
	model.add(Dense(64, kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01), activation='relu'))
	model.add(Dropout(0.25))
	#model.add(Dense(32, kernel_regularizer=l2(0.01), bias_regularizer=l2(0.01), activation='relu'))
	#model.add(Dropout(0.25))
	model.add(Dense(NUMBER_OF_CLASSES, activation='softmax'))
	model.compile(loss=keras.losses.categorical_crossentropy,
				  optimizer=keras.optimizers.Adadelta(),
				  metrics=['accuracy'])
	return model



def train_sets():
	X_train, y_train = get_train_test()
	X_test, y_test = get_validation_test()

	#X_train = X_train.reshape(X_train.shape[0], MFCC_NUM, MAX_MFCC_SHAPE, 1)
	#X_test = X_test.reshape(X_test.shape[0], MFCC_NUM, MAX_MFCC_SHAPE, 1)
	y_train_hot = to_categorical(y_train)
	y_test_hot = to_categorical(y_test)

	yield X_train
	yield X_test
	yield y_train_hot
	yield y_test_hot


# Needs recheck - evaluate?
def get_unknown_speaker_acc(speaker_='theo'):
	
	# Getting the MFCC
	#sample = wav2mfcc('isolation/5B.wav')
	speaker_name = speaker_
	labels, _, _ = get_labels(DATA_PATH)

	correct = OrderedDict([('0', 0), ('1', 0), ('2', 0), ('3', 0), ('4', 0), ('5', 0), ('6', 0),('7', 0), ('8', 0), ('9', 0)])

	for label in labels:
		# Init mfcc vectors
		mfcc_vectors = []

		wavfiles = [DATA_PATH + '/' + label + '/' + wavfile for wavfile in os.listdir(DATA_PATH + '/' + label)]
		wavfiles = [x for x in wavfiles if not x.split("/")[-1].startswith('.')]
		#print wavfiles
		
		wavfiles = [x for x in wavfiles if any(word in x for word in [speaker_name])]
		
		for wavfile in tqdm(wavfiles, desc="Dataset for: " + label):
			#print wavfile
		
			sample = wav2mfcc(wavfile, False)
			# We need to reshape it remember?
			sample_reshaped = sample.reshape(1, MFCC_NUM, MAX_MFCC_SHAPE, 1)
			# Perform forward pass
			prediction = get_labels()[0][
				np.argmax(model.predict(sample_reshaped))
			]
	
			if prediction == label:
				correct[label] += 1


	total = 0
	for i in range(0,10):
		correct[str(i)] = float(correct[str(i)])/float(len(wavfiles))
		total += correct[str(i)]
	
	yield correct
	yield (total/10)*100


def train_cnn(model, batch_n,epochs_n, train_model):

	X_train, X_test, y_train_hot, y_test_hot = train_sets()	

	if train_model:

		checkpoint = keras.callbacks.ModelCheckpoint(filepath=save_model_name, monitor='val_acc', verbose=set_nn_verbosity, save_best_only=True, mode='max')

		early_stopping = keras.callbacks.EarlyStopping(monitor='val_acc', min_delta=0.02, patience=2, verbose=0, mode='max', baseline=None, restore_best_weights=True)

		history = model.fit(X_train, y_train_hot, batch_size=batch_n, epochs=epochs_n, verbose=set_nn_verbosity, validation_data=(X_test, y_test_hot),callbacks=[checkpoint])
	else:
		load_trained_model(save_model_name)
	
	return history
	#return X_test, y_test_hot

def predict_cnn(wave):
	labels, _, _ = get_labels(DATA_PATH)
	
	sample = wav2mfcc(wave,True)
	sample_reshaped = sample.reshape(1,MFCC_NUM, MAX_MFCC_SHAPE)

	prediction = get_labels()[0][
		np.argmax(model.predict(sample_reshaped))
	]

	return prediction
	




def saveHist(path,history):
    new_hist = {}
    for key in list(history.history.keys()):
        if type(history.history[key]) == np.ndarray:
            new_hist[key] == history.history[key].tolist()
        elif type(history.history[key]) == list:
           if  type(history.history[key][0]) == np.float64:
               new_hist[key] = list(map(float, history.history[key]))

    #print(new_hist)
    with codecs.open(path, 'w', encoding='utf-8') as f:
        json.dump(new_hist, f, separators=(',', ':'), sort_keys=True, indent=4) 

def loadHist(path):
    with codecs.open(path, 'r', encoding='utf-8') as f:
        n = json.loads(f.read())
    return n



create_dir([DATA_PATH] + range(0,10))
#create_dir([NN_PATH_DATA_LABELS] + range(0,10))


#create_dir([NN_PATH_DATA,'mfcc','nn_model'])
#save_data_to_array(validation_speaker=validation_speaker)
#save_val_data_to_array(validation_speaker=validation_speaker)


def statistics_plotting(val_speaker='theo'):

	history = loadHist(NN_PATH_DATA_HISTORY+val_speaker)

	# summarize history for accuracy
	plt.plot(history['acc'])
	plt.plot(history['val_acc'])
	plt.title('model accuracy for '+val_speaker)
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()
	# summarize history for loss
	plt.plot(history['loss'])
	plt.plot(history['val_loss'])
	plt.title('model loss for: '+val_speaker)
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.show()

if __name__ == '__main__':
	

	parser = argparse.ArgumentParser(description='We will see about this text..')
	parser.add_argument("-t","--train", help="Train the model again", required=False, action="store_true")
	parser.add_argument("-s","--statistics", help="Output statistics of the model for every speaker", required=False, action="store_true")
	parser.add_argument("-m","--mfcc", help="Re-calculate MFCCs", required=False, action="store_true")
	parser.add_argument("-hi","--history", help="Plot history data from training", required=False, action="store_true")
	parser.add_argument("-sp","--speaker", help="Data for speaker", required=False)
	parser.add_argument("-e","--epochs", help="Change epochs of training", required=False)
	args = parser.parse_args()


	acc = []
	if args.speaker:
		del speakers_[:]
		speakers_.append(args.speaker)
	for sp in speakers_:
		validation_speaker = sp
		print "SPEAKER VAILIDATOR: ", validation_speaker
		save_model_name = os.path.join(NN_PATH_DATA + "/nn_model/"+validation_speaker+"_model_auto.h5")
		
		if args.mfcc:
			save_data_to_array(validation_speaker=sp)
			save_val_data_to_array(validation_speaker=sp)

		model = neural_network_model()

		batch_number = 100
		epochs_number = 100

		if args.epochs:
			try: 
				ep = int(args.epochs)
				epochs_number = ep
			except:
				epochs_number = 100

		if args.train:
			history = train_cnn(model, batch_number,epochs_number, True,)
			saveHist(NN_PATH_DATA_HISTORY+validation_speaker,history)
		
		load_trained_model(save_model_name)
		if args.statistics:
			_, X_test, _, y_test_hot = train_sets()	
			outdata = model.evaluate(X_test,y_test_hot)
			acc.append(outdata[1])
			print outdata

		if args.history:
			statistics_plotting(validation_speaker)

	if args.statistics:
		print "total: ", sum(acc)/len(acc)
	exit()
	#get_train_test()

validation_speaker = "lena"
save_model_name = os.path.join(NN_PATH_DATA + "/nn_model/"+validation_speaker+"_model_auto.h5")
model = neural_network_model()




