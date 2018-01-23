#!/usr/local/bin/python3

import sys
import freq
import random

def pseudoSequence(trainingFile, seqLen = 20000, order = 3):
	with open(trainingFile) as tFile:
		tFile.readline()
		seq = tFile.read().replace("N", "A").replace("\n", "")
	print(">RandomSequence\n")
	piSet = freq.nucFreq(trainingFile)
	samp1, samp2 = freq.countNuc(seq, order -1), freq.countNuc(seq, order)
	newSeq = ""	
	A = piSet["A"]
	T = A + piSet["T"]
	C = T + piSet["C"]
	G = C + piSet["G"]

	random.seed()
	#first order length sequence -- assumes independence	
	for i in range(0, order):
		bp = random.random()
		if bp <= T:
			newSeq += ("A" if bp <= A else "T") 
		else:
			newSeq += ("C" if bp <= C else "G")

	#getting the next order - seqLen bp in the sequence
	for i in range(0, seqLen - order):
		A = samp2[newSeq[i:] + "A"] / samp1[newSeq[i:]]
		T = A + samp2[newSeq[i:] + "T"] / samp1[newSeq[i:]]
		C = T + samp2[newSeq[i:] + "C"] / samp1[newSeq[i:]]
		G = C + samp2[newSeq[i:] + "G"] / samp1[newSeq[i:]]
		bp = random.random()
		if bp <= T:
			newSeq += ("A" if bp <= A else "T") 
		else:
			newSeq += ("C" if bp <= C else "G")
		
	for i in range(0, len(newSeq), 70):
		print(newSeq[i: i+70])
	return newSeq


if __name__ == "__main__":
	trainingFile = "human_mito.fasta" if len(sys.argv) < 2 else str(sys.argv[1])
	len(pseudoSequence(trainingFile))
