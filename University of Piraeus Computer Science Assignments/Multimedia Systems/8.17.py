import imageio
import numpy as np
from scipy.stats import entropy
import matplotlib.pyplot as plt
import os
import time
from tqdm import tqdm_notebook
from ipywidgets import IntProgress

def EntropiaIkonas(img, k=2):
    _, i = np.unique(img, return_counts=True)
    return entropy(i, base=k)
	
def seeVideoFrames(file):
    video = imageio.get_reader(file,  'ffmpeg')
    fps = video.get_meta_data()['fps']
    i = 0
    frames = []
    while 1:
        try:
            img = video.get_data(i)
            frames.append(img)
            i+=1
        except IndexError:
            break

    return np.array(frames), fps
	
def aspromauro(egxrwmovideo):
    '''Converts numpy array vid to grayscale vid'''
    framesblacknwhite = []
    for i in egxrwmovideo:
        framesblacknwhite.append(np.around(np.dot(i[:,:,:3], [0.2989, 0.587, 0.114])))
    return np.array(framesblacknwhite)
	
def DiaforaFrames(frames):
    diflist = []
    for i in range(1, frames.shape[0]):
        diflist.append(frames[i,:,:]-frames[i-1,:,:])
    return np.array(diflist)
	
def makeMacroblocks(frame, macroblocksize=16):
    macroblocks = []
    k, l = frame.shape
    for i in range(0, k, macroblocksize):
        for j in range(0, l, macroblocksize):
            macroblock = frame[i:i+macroblocksize,j:j+macroblocksize]
            if macroblock.shape == (macroblocksize, macroblocksize):
                macroblocks.append(macroblock)
            else:
                try:
                    macroblock = np.vstack((macroblock, np.zeros(macroblock.shape[0], macroblocksize-macroblock.shape[1])))
                except TypeError:
                    pass
                try:
                    macroblock = np.hstack((macroblock, np.zeros(macroblocksize-macroblock.shape[0], macroblock.shape[1])))
                except TypeError:
                    pass
                macroblocks.append(macroblock)
    return np.array(macroblocks).reshape((int(k/macroblocksize), int(l/macroblocksize), macroblocksize, macroblocksize))
	
def createNeighborhood(referenceFrame, indexOfMacroblock, macroblocksize=16, k=16):
    neighborhood = []
#     print (indexOfMacroblock)
    for i in range(indexOfMacroblock[0]-k, indexOfMacroblock[0]+k+1, k):
        for j in range(indexOfMacroblock[1]-k, indexOfMacroblock[1]+k+1, k):
            if (i >= 0 and j >= 0 and i+macroblocksize < referenceFrame.shape[0] and j+macroblocksize < referenceFrame.shape[1]):
#                 print (i,j)
                neighborhood.append(referenceFrame[i:i+macroblocksize, j:j+macroblocksize])
            else:
                neighborhood += [None]
    return neighborhood
	
def SAD(referenceMacroblock, targetMacroblock):
#     print (targetMacroblock.shape, referenceMacroblock.shape)
    return np.sum(np.abs(targetMacroblock - referenceMacroblock))
	
def calculateSAD(targetMacroblock, referenceFrame_neighbor_macroblocks):
    SADvals = []
        
    for macroblock in referenceFrame_neighbor_macroblocks:
        if macroblock is not None:
            SADvals.append(SAD(macroblock, targetMacroblock))
        else:
            SADvals.append(np.Inf)
    
    return np.array(SADvals).reshape((3,3))
	
def logarithmicSearch(referenceFrame, targetMacroblock, indexOfMacroblock, macroblocksize=16, k=16):
    if (k == 0):
        return indexOfMacroblock, referenceFrame[indexOfMacroblock[0]:indexOfMacroblock[0]+macroblocksize, indexOfMacroblock[1]:indexOfMacroblock[1]+macroblocksize] # motionVector END (To_WIDTH, To_HEIGHT), return Predicted Frame
    
    referenceFrame_neighbor_macroblocks = createNeighborhood(referenceFrame, indexOfMacroblock, macroblocksize, k)

    SAD_values = calculateSAD(targetMacroblock, referenceFrame_neighbor_macroblocks)
#     print (SAD_values)
    indexofMinimumSAD = divmod(SAD_values.argmin(), SAD_values.shape[1])
    newIndexOfMacroblock = list(indexOfMacroblock)
    
    if (indexofMinimumSAD[0] == 0):
        newIndexOfMacroblock[0] = indexOfMacroblock[0] - k
    elif (indexofMinimumSAD[0] == 2):
        newIndexOfMacroblock[0] = indexOfMacroblock[0] + k
    
    if (indexofMinimumSAD[1] == 0):
        newIndexOfMacroblock[1] = indexOfMacroblock[1] - k
    elif (indexofMinimumSAD[1] == 2):
        newIndexOfMacroblock[1] = indexOfMacroblock[1] + k

    if (indexofMinimumSAD[0] == 1 and indexofMinimumSAD[1] == 1):
        newK = k//2
    else:
        newK = k       
#     print (indexofMinimumSAD)
#     print (newIndexOfMacroblock)
    return logarithmicSearch(referenceFrame, targetMacroblock, tuple(newIndexOfMacroblock), macroblocksize, newK)
	
def motionCompensation(referenceFrame, targetFrame, macroblocksize=16):
    predictedBlocks = []
    motionVectors = []
    
    targetMacroblocks = makeMacroblocks(targetFrame, macroblocksize)
    for i in range(targetMacroblocks.shape[0]):
        for j in range(targetMacroblocks.shape[1]):
            motionVectorSTART = (i*macroblocksize, j*macroblocksize)
            indexofBlock = (i*macroblocksize, j*macroblocksize)
            motionVectorEND, prediction = logarithmicSearch(referenceFrame, targetMacroblocks[i,j,:,:], indexofBlock)
            predictedBlocks.append(prediction)
            motionVectors.append(motionVectorSTART+motionVectorEND)

#     print (len(motionVectors))
    predictedBlocks = np.array(predictedBlocks).reshape(targetMacroblocks.shape)
    motionVectors = np.array(motionVectors, dtype=(int,4)).reshape((targetMacroblocks.shape[0], targetMacroblocks.shape[1], 4))
    return predictedBlocks, motionVectors
	
def imageReconstructFromBlocks(blocks):
    lines = []
    for i in range(blocks.shape[0]):
        line = []
        for j in range(blocks.shape[1]):
            line.append(blocks[i,j,:,:])
        line = np.hstack(line)
        lines.append(line)
    return np.vstack(lines)
	

	
	
	
hall_monitor_cif = "resources\ex817\sample1.mp4"
# hall_monitor_cif = "resources\ex817\sample2.mp4"
resources_path = "resources\ex817"

videoFrames, fps = seeVideoFrames(hall_monitor_cif)
videoFramesSample = videoFrames[:, :, :, :]
videoFramesSample.shape
videoFramesSample = aspromauro(videoFramesSample)
videoFramesSample.shape

frameDifferenceSample = DiaforaFrames(videoFramesSample)
frameDifferenceSample.shape

plt.imshow(videoFramesSample[50], cmap='gray')
plt.imshow(videoFramesSample[51], cmap='gray')
plt.imshow(frameDifferenceSample[50], cmap='gray')

avg = 0
for frame in videoFramesSample:
    avg += EntropiaIkonas(frame)
avg /= videoFramesSample.shape[0]
avg

compensatedVideoFramesSample = [videoFramesSample[0]]
motionVectors = []
for prevFrame, nextFrame in tqdm_notebook(zip(videoFramesSample, videoFramesSample[1:]), total=len(videoFramesSample[1:])):
    prediction, vectors = motionCompensation(prevFrame, nextFrame)
    predFrame = imageReconstructFromBlocks(prediction)
    compensatedVideoFramesSample.append(predFrame)
    motionVectors.append(vectors)
	
compensatedFrameDifferenceSample = DiaforaFrames(np.array(compensatedVideoFramesSample).reshape(videoFramesSample.shape))
compensatedFrameDifferenceSample.shape

plt.imshow(compensatedVideoFramesSample[50], cmap='gray')
plt.imshow(compensatedVideoFramesSample[51], cmap='gray')
plt.imshow(compensatedFrameDifferenceSample[50], cmap='gray')

avgCompensated = 0
for compensatedFrame in compensatedVideoFramesSample:
    avgCompensated += EntropiaIkonas(compensatedFrame)
avgCompensated /= videoFramesSample.shape[0]
avgCompensated
print(avgCompensated)

writer  =  imageio.get_writer(os.path.join(resources_path,'sample1_motion_compensated.mp4'), fps=fps,mode="I")

for frame in compensatedVideoFramesSample:
    writer.append_data(frame)
writer.close()
