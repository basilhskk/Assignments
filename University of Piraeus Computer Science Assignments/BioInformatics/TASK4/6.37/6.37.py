def check_seq(sequence, position, ACount, CCount):
    if sequence[position]=='A':
        ACount+=1
        CCount = 0
        if ACount == 5:
            ACount = 0
            return True
        elif sequence[position] != sequence[position+1]:
            return True
    elif sequence[position]=='C':
        CCount+=1
        ACount = 0
        if CCount == 10:
            CCount = 0
            return True
        elif sequence[position] != sequence[position+1]:
            return True
    else:
        CCount = 0
        ACount = 0
        if sequence[position] != sequence[position+1]:
            return True
    return False

seqFile = open("./6.37Sequence/nucleotide.txt", "r")
seq = []
lines = seqFile.readlines()[1:]
for line in lines:
    for letter in line:
        seq.append(letter)
seqFile.close()

newSeq = []
ACount = 0
CCount = 0
for i in range(len(seq)-1):
    if(check_seq(seq,i,ACount,CCount)):
        newSeq.append(seq[i])
if(check_seq(seq,len(seq)-2,ACount,CCount)):
    newSeq.append(seq[-1])
print(newSeq)