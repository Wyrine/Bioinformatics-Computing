#!/usr/local/bin/python3

#Kirolos Shahat
#geno.py -- generate a randomSequence based off of a training
#model that is a fasta file

import sys
import freq
import random

def pseudoSequence(trainingFile, seqLen = 20000, order = 3):
	""" Generate a random sequence of DNA based off of a training file
			and it's frequencies. The first order number of elements are
			purely dependent on pr(x) where x in {A,C,T,G} and thus are independent
			while the rest are conditionally based on the previous sequence of length
			order. seqLen is defaulted to 20k and order is defaulted to 3
	"""
	with open(trainingFile) as tFile:
		tFile.readline()
		seq = tFile.read().replace("N", "A").replace("\n", "")
	print(">RandomSequence\n")
	#pr(x) 
	piSet = freq.nucFreq(trainingFile)
	#count of order and order -1 elements
	samp1, samp2 = freq.countNuc(seq, order -1), freq.countNuc(seq, order)
	newSeq = ""	
	#Setting the range to choose a specific base given a random number between [0, 1)
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
		#Setting the range given conditional probabilities which sum to 1
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
	print(pseudoSequence(trainingFile))
