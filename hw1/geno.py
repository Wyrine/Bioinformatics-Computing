#!/usr/local/bin/python3

import sys
import freq

def pseudoSequence(outputName, trainingFile, seqLen = 20000, order = 3):
	with open(trainingFile) as tFile:
		first = tFile.readline().split(" ")
		seq = tFile.read().replace("N", "A").replace("\n", "")
	first[0] = ">RandomSequence"
	first = " ".join(first)
	with open(outputName, "w+") as out:
		out.write(first + "\n")	
		piSet = freq.nucFreq(trainingFile)
		samp1, samp2 = freq.countNuc(seq), freq.countNuc(seq, order)
		bp, high = "", -1
		for k, v in piSet.items():
			if v > high:
				bp, high = k, v	
		newSeq = ""	
		for i in range (0, order):
			newSeq += k
		for i in range(order, seqLen):
			pass	


if __name__ == "__main__":
	trainingFile = "human_mito.fasta"
	output = "random_sequence.fasta"
	pseudoSequence(output, trainingFile)
