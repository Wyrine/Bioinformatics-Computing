#!/usr/local/bin/python3

#Kirolos Shahat
#prob.py -- gets the multinomial and markov probability of a test
#sequence given a training sequence, both in fasta format, and gets
#them into a log scale to protect against underflow

import sys
from math import log
from freq import nucFreq, countNuc 

def getMultiProb(testingFile, baseProbability):
	""" given a testingFile, which is a fasta file, and
			baseProbability, which is a dictionary of 
			probabilities for each nucleotide. The function
			uses the multinomial sequence model and receives
			the probability of that sequence and converts it
			into a log base e scale
	"""

	with open(testingFile) as test:
		test.readline()
		testSequence = test.read().replace("N", "A")
	probab = {}
	#Assume independence, thus pr(AA) = pr(A) ** 2
	for key in "ACGT":
		probab[key] = testSequence.count(key) * log(baseProbability[key]) 
	testMulti = 0
	for val in probab.values():
		testMulti += val
	return testMulti

#yet to work for order = 0
#goal to fix given free time
def getMarkovProb(testingFile, trainingFile, piSet, order = 3):
	""" given a testingFile fasta file, trainingFile fasta file,
			a piSet which is a dictionary of the probabilities of each nucleotide 
			in the training sequence, and an optional order (default order = 3) computes
			the markovProbability of the testing sequence trained off of the
			training file. The probability is given on a log scale to ensure that
			there is no underflow.
	"""
	with open(testingFile) as test:
		test.readline()
		seq = test.read().replace("N", "A").replace("\n", "")
	markovProb = 1
	#order = 0
	#Opening the file to get the count of length (order - 1) and (order)
	#stored in samp1 and samp2 respectively.	
	with open(trainingFile) as fastFile:
		fastFile.readline()
		trainSeq = fastFile.read().replace("N", "A").replace("\n", "")
	if order > 0: 
		samp1 = countNuc(trainSeq, order - 1)
	samp2 = countNuc(trainSeq, order)
	
	#getting the non-conditional probabilities added to 
	#the markovProb
	for i in range (0, order):
		markovProb *= piSet[seq[i]]
	#unlikely to underflow before this point, this optimize slightly
	markovProb = log(markovProb)
	for i in range (0, len(seq) - order):
		#current substring of length order
		temp = seq[i:i+order+1]
		markovProb += log(samp2[temp])
		#my attempt at making it both multinomial and markov
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
	#to print to report.txt properly
	logMultiProb = getMultiProb(testingFile, baseProbability)
	print("\t Log probability (multinomial):", logMultiProb)
	logMarkProb = getMarkovProb(testingFile, trainingFile, baseProbability, 3)
	print("\t Log probability (markov):", logMarkProb)
