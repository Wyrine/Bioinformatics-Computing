#!/usr/local/bin/python3

import sys
from math import log
import freq

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
	#Assume independence, thus pr(A*A) = pr(A) ** 2
	for key in "ACGT":
		probab[key] = baseProbability[key] ** testSequence.count(key)
	testMulti = 1
	for val in probab.values():
		testMulti *= val
	return log(testMulti)

def getMarkovProb(testingFile, baseProbability, order):
	with open(testingFile) as test:
		test.readline()
		seq = test.read().replace("N", "A").replace("\n", "")
	freq = {}
	for index in range(0, len(seq) - order):
		temp = seq[index:index+order+1]
		if temp not in freq:
			freq[temp] = 0
		freq[temp] += 1
	probBP = {}
	markProb = 0
	for k, v in freq.items():
		freq[k] = v/ (len(seq) - order)
		if k[-1] not in probBP:
			probBP[k[-1]] = freq[k]
		else:
			probBP[k[-1]] *= freq[k]
	for k, v in probBP.items():
				markProb += log(v) + log(baseProbability[k])
	print(markProb)


if __name__ == "__main__":
	trainingFile = "human_mito.fasta"
	testingFile = "neander_sample.fasta"
	if len(sys.argv) == 3:
		trainingFile = str(sys.argv[1])
		testingFile = str(sys.argv[2])
	baseProbability = freq.nucFreq(trainingFile)
	trainVal = 1
	for val in baseProbability.values():
		trainVal *= val
	logMultiProb = getMultiProb(testingFile, baseProbability)
	print("Log probability (multinomial):", logMultiProb)
	logMarkProb = getMarkovProb(testingFile, baseProbability, 3)
