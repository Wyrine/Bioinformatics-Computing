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
		testSequence = test.read().splitlines()
	del testSequence[0]
	testSequence = "".join(testSequence)
	testSequence = testSequence.replace("N", "A")
	probab = {}
	#Assume independence, thus pr(A*A) = pr(A) ** 2
	for key in "ACGT":
		probab[key] = baseProbability[key] ** testSequence.count(key)
	testMulti = 1
	for val in probab.values():
		testMulti *= val
	return log(testMulti)

def getConditionalMultiProb(trainVal, testVal):
	ratio = testVal / trainVal
	return log(ratio)

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
