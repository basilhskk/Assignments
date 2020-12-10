import numpy as np
import random
from scipy.fftpack import dct
import re

def Dct(image):
    for i in range(image.ndim):
        image = dct(image, axis=i, norm="ortho")
    return image

def fives(num):
    x = random.randint(0, 4)
    str1 = str(num)
    arr1 = list(str1)
    arr1[x] = '5'
    str1 = ''.join(arr1)
    num = int(str1)
    return num

def Macroblocking(image, macrob_size):
    macroblocks = {}
    w, h = image.shape
    for i in range(w):
        for j in range(h):
            macroblocks[(i, j)] = image[i*macrob_size:i*macrob_size+macrob_size, j*macrob_size:j*macrob_size+macrob_size]
    return macroblocks

dictionary = {}
def frequency (string) :
    freqs = {}
    for ch in string :
        freqs[ch] = freqs.get(ch,0) + 1
    return freqs

def sortFreq (freqs) :
    letters = freqs.keys()
    tuples = []
    for let in letters :
        tuples.append((freqs[let],let))
    tuples.sort()
    return tuples

def buildTree(tuples) :
    while len(tuples) > 1 :
        firstTwo = tuple(tuples[0:2])                 
        theRest  = tuples[2:]                          
        combFreq = firstTwo[0][0] + firstTwo[1][0]     
        tuples   = theRest + [(combFreq,firstTwo)]    
        tuples.sort(key=lambda t: t[0])                               
    return tuples[0]            

def trimTree (tree) :
     # Trim the freq counters off, leaving just the letters
    p = tree[1]                                    
    if type(p) == type("") : return p              
    else : return (trimTree(p[0]), trimTree(p[1])) 

def coding(node, pat='') :
    global dictionary
    if type(node) == type("") :
        dictionary[node] = pat                
    else  :                              
        coding(node[0], pat+"0")   
        coding(node[1], pat+"1")   
def encode(string) :
    global dictionary
    output = ""
    for ch in string : output += dictionary[ch]
    return output

def decode(tree, string) :
    dec = ""
    p = tree
    for bit in string :
        if bit == '0' : p = p[0]     
        else          : p = p[1]    
        if type(p) == type("") :     
            dec += p              
            p = tree                
    return dec

def huff(string) :
    freqs = frequency(string)
    tuples = sortFreq(freqs)
    tree = buildTree(tuples)
    tree = trimTree(tree)
    coding(tree)
    enc = encode(string)
    dec = decode (tree, enc)
    return enc, dec

imageA = []
imageB = []
str1 = 0
str2 = 0
Ai=[16057,16066]

for times in range(0,100):
    imageA = np.zeros((104, 200), dtype=int) + random.choice(Ai)   
    for i in range(104):
        for j in range(200):
            imageA[i][j] = fives(imageA[i][j])
   
    macroblocks = Macroblocking(imageA, 8)
    strA, decA = huff(re.sub('\ |\?|\.|\!|\/|\;|\:|\]|\[','', str(imageA)))
    str1 += int(len(strA))
    imageB = Dct(imageA)
    strB, decB = huff(re.sub('\ |\?|\.|\!|\/|\;|\:|\]|\[','', str(imageB)))
    str2 += int(len(strB))

compress_ratio = (str2/str1)
print("{:.3f}".format(compress_ratio))