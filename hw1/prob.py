#!/usr/local/bin/python3

import sys
from math import log
from freq import nucFreq, countNuc 

def getMultiProb(testingFile, baseProbability):
	""" Given base probabilities as a dictionary parameter
			from a training sequence, calculates the probability
			the testing sequence assuming independent probabilities
			in the base appearance pattern.
	"""
	with open(testingFile) as test:
		test.readline()
		testSequence = test.read().replace("N", "A")
	probab = {}
	#Assume independence, thus pr(AA) = pr(A) ** 2
	for key in "ACGT":
		probab[key] = baseProbability[key] ** testSequence.count(key)
	testMulti = 1
	for val in probab.values():
		testMulti *= val
	return log(testMulti)

#yet to work for order = 0
def getMarkovProb(testingFile, trainingFile, piSet, order = 1):
	with open(testingFile) as test:
		test.readline()
		seq = test.read().replace("N", "A").replace("\n", "")
	markovProb = 1
	#order = 0	
	with open(trainingFile) as fastFile:
		fastFile.readline()
		trainSeq = fastFile.read().replace("N", "A").replace("\n", "")
	if order > 0: 
		samp1 = countNuc(trainSeq, order - 1)
	samp2 = countNuc(trainSeq, order)
	
	#multinomial for the first order number of bps
	for i in range (0, order):
		markovProb *= piSet[seq[i]]
	markovProb = log(markovProb)
	for i in range (0, len(seq) - order):
		temp = seq[i:i+order+1]
		markovProb += log(samp2[temp])
		if order > 0:
			markovProb -= log(samp1[temp[:-1]])
	return markovProb


if __name__ == "__main__":
	trainingFile = "human_mito.fasta"
	testingFile = "neander_sample.fasta"
	if len(sys.argv) == 3:
		trainingFile = str(sys.argv[1])
		testingFile = str(sys.argv[2])
	baseProbability = nucFreq(trainingFile)
	trainVal = 1
	for val in baseProbability.values():
		trainVal *= val
	logMultiProb = getMultiProb(testingFile, baseProbability)
	print("\t Log probability (multinomial):", logMultiProb)
	logMarkProb = getMarkovProb(testingFile, trainingFile, baseProbability, 3)
	print("\t Log probability (markov):", logMarkProb)
