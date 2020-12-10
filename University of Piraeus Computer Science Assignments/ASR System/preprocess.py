from __future__ import division 
from scipy.io import wavfile
from scipy import signal
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
import librosa
import IPython.display as ipd
from endpoints import endpoints
import math
from itertools import groupby, count
import wave


Fs = 8000
NS=30
L = NS*Fs/1000
MS = 10
R = MS*Fs/1000

def filter(wave,sr):

	# Band-pass Filter
	if sr != 8000:

		fL = 100/float(sr)  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
		fH = 4000/float(sr)  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
		b = 200/float(sr)  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).
		N = int(np.ceil((4 / b)))
		if not N % 2: N += 1  # Make sure that N is odd.
		n = np.arange(N)
		 
		# Compute a low-pass filter with cutoff frequency fH.
		hlpf = np.sinc(2 * fH * (n - (N - 1) / 2))
		hlpf *= np.blackman(N)
		hlpf = hlpf / np.sum(hlpf)
		 
		# Compute a high-pass filter with cutoff frequency fL.
		hhpf = np.sinc(2 * fL * (n - (N - 1) / 2))
		hhpf *= np.blackman(N)
		hhpf = hhpf / np.sum(hhpf)
		hhpf = -hhpf
		hhpf[(N - 1) // 2] += 1
		 
		# Convolve both filters.
		h = np.convolve(hlpf, hhpf)

		wave = np.convolve(wave, h)

		wave = wave/max(-min(wave), max(wave))
		#wave = bandpass_filter(wave,100,4000,25,sr)
		# STEP 2 - Resample input signal
		x_wave = librosa.resample(wave.astype(float), sr, Fs)
	else: # High-pass Filter
		fc = 0.0125  # Cutoff frequency as a fraction of the sampling rate (in (0, 0.5)).
		b = 0.025  # Transition band, as a fraction of the sampling rate (in (0, 0.5)).
		N = int(np.ceil((4 / b)))
		if not N % 2: N += 1  # Make sure that N is odd.
		n = np.arange(N)
		 
		# Compute a low-pass filter.
		h = np.sinc(2 * fc * (n - (N - 1) / 2))
		w = np.blackman(N)
		h = h * w
		h = h / np.sum(h)
		 
		# Create a high-pass filter from the low-pass filter through spectral inversion.
		h = -h
		h[(N - 1) // 2] += 1

		wave = np.convolve(wave, h)

		wave = wave/max(-min(wave), max(wave))
		#wave = bandpass_filter(wave,100,4000,25,sr)
		x_wave = wave
	return x_wave
	
def wav_preprocess(fName):
	# STEP 1 - Load speech file and normalize it
	wave, sr = librosa.load(fName, mono=True, sr=None)
	

	x_wave = filter(wave,sr)

	return x_wave

def energy_zerocrossings(x_wave):
	totalSamples=len(x_wave)
	ss = 1
	energy = []
	zero_crossings = []

	while(ss+L <= totalSamples): 
		frame = x_wave[ss:int(ss+L)]*np.hamming(L)
		energy.append(10*math.log10(np.sum(frame**2))) # maybe use: np.concatenate((a,a))

		zero_crossings.append(np.sum(np.abs(np.diff(np.sign(frame))))) #np.nonzero(np.diff(frame > 0))[0]) # THIS NEEDS TO BE CHECKED
		ss = int(ss+R)
	return energy, zero_crossings




# STEP 6 - Calc avg standards deviation
def deviations(energy,zero_crossings):
	trainingFrames = 10
	# eavg
	yield np.mean(energy[1:trainingFrames+1]) 
	#esig 
	yield np.std(energy[1:trainingFrames+1])
	#zcavg
	yield np.mean(zero_crossings[1:trainingFrames+1])
	#zcsig
	yield np.std(zero_crossings[1:trainingFrames+1])


def detection_params(energy, eavg, esig, zcavg, zcsig):
	#IF 
	IF = 35
	yield IF
	#IZCT 
	IZCT = max(IF,zcavg+3*zcsig)
	yield IZCT
	#IMX
	IMX = max(energy)
	yield IMX
	#ITU
	ITU = IMX - 20
	yield ITU
	#ITL
	yield max(eavg+3*esig, ITU-20)
