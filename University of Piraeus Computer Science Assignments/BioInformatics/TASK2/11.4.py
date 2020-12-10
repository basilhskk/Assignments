import numpy as np

d = 'ACGT'

x_old = 'GGCT'

x = []

#protein to numbers
for i in range(0,len(x_old)):
    if(x_old[i] == d[0]) :
        x.append(0)
    elif(x_old[i] == d[1]) :
        x.append(1)
    elif(x_old[i] == d[2]) :
        x.append(2)
    elif(x_old[i] == d[3]) :
        x.append(3)
    else:
        print("Invalid Input")
        exit()
    
#chances 
A = [[0.9,0.1],[0.1,0.9]]

B = [[0.4,0.4],[0.1,0.1],[0.2,0.2],[0.3,0.3]]

# Init chances for begin state
pi_init = [[0.5],[0.5]]

# Number of states
N = len(A[0])

#Number of nucleotids
M = len(B[0])

# Length of the sequence
T = len(x)

# Create score matrix
c = np.zeros((N,T)).tolist()
# Create an array of the paths that followed
paths = np.zeros((N,T),int).tolist()

print(paths)
# Init

for i in range(0,N):
    c[i][0] = np.log10(pi_init[0]).tolist()[0]+np.log10(B[x[0]][i]) 

# Iteration for every number of sequence

for t in range(1,T): # 2nd to the last
    for i in range(0,N): #for every state 
        # N different scores, in which I choose the greatest
        v = np.zeros((1,N)).tolist()[0]

        for p in range(0,N): # from each predecessor
            v[p] = c[p][t-1] + A[p][i] * B[x[t]][i]  
        c[i][t]  = max(v)
        ind = v.index(max(v))
        paths[i][t]  = ind

# Find best route
bp = [c.index(max(c))]

t=0
for t in range(0,3):
    ind = paths[bp[-1]][t]
    bp.append(ind)

# Find Viterbi score
score = 1
for t in range(0,T):
    score = score * c[bp[t]][t]

# Convert numbers to state names
sequence = []
for i in range(0,T):
    if bp[i] == 0:
        sequence.append('a')
    elif bp[i] == 1:
        sequence.append('b')

print( 'States sequence is: ' + str(sequence))