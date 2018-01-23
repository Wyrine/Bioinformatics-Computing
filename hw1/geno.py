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
		samp1, samp2 = freq.countNuc(seq, order -1), freq.countNuc(seq, order)
		bp, high = "", -1
		for k, v in piSet.items():
			if v > high:
				bp, high = str(k), v	
		newSeq = ""	
		for i in range(0, order):
			newSeq += bp
		print(newSeq)
		for i in range(order, seqLen):
			subSeq = newSeq[i:]
			bp, high = "", -1
			for x in "ACTG":
				prob = samp2[subSeq + x] / samp1[subSeq]
				if prob > high:
						bp = x
						high = prob
			newSeq += bp
		for i in range(0, len(newSeq), 70):
			out.write(newSeq[i: i+70] + "\n")
		out.write("\n")
		return newSeq


if __name__ == "__main__":
	trainingFile = "human_mito.fasta"
	output = "random_sequence.fasta"
	pseudoSequence(output, trainingFile)
