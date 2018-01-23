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
	
	A = piSet["A"]
	T = A + piSet["T"]
	C = T + piSet["C"]
	G = C + piSet["G"]
	#setting the highest probability sequence for the first order number of elements
	newSeq = ""	
	random.seed()
	
	for i in range(0, order):
		bp = random.random()
		if bp <= T:
			newSeq += ("A" if bp <= A else "T") 
		else:
			newSeq += ("C" if bp <= C else "G")
	for i in range(0, seqLen):
		bp, high = "", -1
		for x in "ACTG":
			prob = samp2[newSeq[i:] + x] / samp1[newSeq[i:]]
			if prob > high:
				high = prob
				bp = x
		newSeq = newSeq + bp
	for i in range(0, len(newSeq), 70):
		print(newSeq[i: i+70])
	print("\n")
	return newSeq


if __name__ == "__main__":
	trainingFile = "human_mito.fasta"
	pseudoSequence(trainingFile)
