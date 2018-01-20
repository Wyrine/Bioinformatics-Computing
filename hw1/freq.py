#!/usr/local/bin/python3

import sys

def nucFreq(fileName):
	""" compute the frequency of each nucleotide in fileName which
			is assumed to be a fasta file. Returns a dictionary of size 4
	"""
	numFreqs = {}
	with open(fileName) as fastFile:
		lines = fastFile.read().splitlines()
	del lines[0]
	seq = "".join(lines)	
	numFreqs['A'] = seq.count("A") + seq.count("N")	
	numFreqs['C'] = seq.count("C")	
	numFreqs['G'] = seq.count("G")	
	numFreqs['T'] = seq.count("T")	
	for char in "ACGT":
		numFreqs[char] /= len(seq)
	return numFreqs

def diNucFreq(fileName):
	""" Computes the frequency of each dinucleotide in fileName
			which is assumed to be a fasta file. Returns a dictionary of
			size 16
	"""
	numFreqs = {}
	for first in "ACGT":
		for second in "ACGT":
			numFreqs[first + second] = 0
	with open(fileName) as fastFile:
		lines = fastFile.read().splitlines()
	del lines[0]
	seq = "".join(lines)
	seq = seq.replace("N", "A")
	#wanted to use count here as well but it did not give the proper
	#value because "AAA".count("AA") = 1 but it should be 2
	for i in range(0, len(seq) - 1):
		numFreqs[seq[i] + seq[i+1]] += 1
	for key in numFreqs:
		numFreqs[key] /= len(seq)
	return numFreqs

if __name__ == "__main__":
	fileName = "lambda.fasta"
	if len(sys.argv) == 2:
		fileName = str(sys.argv[1])
	print("\t Nucleotide Frequences:")
	for key, val in nucFreq(fileName).items():
		print("\t " + str(key) + ":", str(val)) 
	print("\t Dinucleotide Frequencies:")
	for key, val in diNucFreq(fileName).items():
		print("\t " + str(key) + ":", str(val)) 
