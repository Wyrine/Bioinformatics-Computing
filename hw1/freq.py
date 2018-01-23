#!/usr/local/bin/python3

#Kirolos Shahat
#freq.py -- contains countNuc and nucFreq functions

import sys

def countNuc(seq, n = 0):
	""" countNuc is a function that takes a sequence
			of any kind and generates a dictionary of counts
			(n+1) - mers keyed on the name.
	"""
	countDict = {}
	for index in range(0, len(seq) - n):
		temp = seq[index: index + n + 1]
		if temp not in countDict:
			countDict[temp] = 0
		countDict[temp] += 1
	return countDict
		
def nucFreq(fileName, n = 0):
	""" Computes the frequency of each (n+1)-nucleotide in fileName
			which is assumed to be a fasta file. Returns a dictionary of
			size 4^(n+1) of the frequency of each (n+1)-mer
	"""
	with open(fileName) as fastFile:
		fastFile.readline()
		seq = fastFile.read().replace("N", "A").replace("\n", "")
	numFreqs = countNuc(seq, n)
	for key in numFreqs:
		numFreqs[key] /= (len(seq) - n)
	return numFreqs

if __name__ == "__main__":
	fileName = "lambda.fasta" if len(sys.argv) < 2 else fileName = str(sys.argv[1])
	#the following was done to print neatly into report.txt
	print("\t Nucleotide Frequences:")
	nuc = nucFreq(fileName)
	for key in "ACGT":
		print("\t " + str(key) + ":", str(nuc[key])) 
	print("\t Dinucleotide Frequencies:")
	diNuc = nucFreq(fileName, 1)
	for bp1 in "ACGT":
		for bp2 in "ACGT":
			print("\t " + bp1 + bp2 + ":", diNuc[bp1+bp2])
