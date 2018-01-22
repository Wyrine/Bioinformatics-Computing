#!/usr/local/bin/python3

import sys

def nucFreq(fileName, n = 0):
	""" Computes the frequency of each dinucleotide in fileName
			which is assumed to be a fasta file. Returns a dictionary of
			size 16
	"""
	numFreqs = {}
	with open(fileName) as fastFile:
		fastFile.readline()
		seq = fastFile.read().replace("N", "A").replace("\n", "")
	#wanted to use count here but it did not give the proper
	#value because "AAA".count("AA") = 1 but it should be 2
	for i in range(0, len(seq) - n):
		temp = seq[i:i+n + 1]
		if temp not in numFreqs:
			numFreqs[temp] = 0
		numFreqs[temp] += 1
	for key in numFreqs:
		numFreqs[key] /= (len(seq) - n)
	return numFreqs

if __name__ == "__main__":
	fileName = "lambda.fasta"
	if len(sys.argv) == 2:
		fileName = str(sys.argv[1])
	print("\t Nucleotide Frequences:")
	nuc = nucFreq(fileName)
	for key in "ACGT":
		print("\t " + str(key) + ":", str(nuc[key])) 
	print("\t Dinucleotide Frequencies:")
	diNuc = nucFreq(fileName, 1)
	for bp1 in "ACGT":
		for bp2 in "ACGT":
			print("\t " + bp1 + bp2 + ":", diNuc[bp1+bp2])
