#!/usr/local/bin/python3

import sys
#from rev import reverseComplement

def nucFreq(fileName):
	numFreqs = {}
	with open(fileName) as fastFile:
		lines = fastFile.read().splitlines()
	del lines[0]
	seq = "".join(lines)	
	numFreqs['A'] = seq.count("A") + seq.count("N")	
	numFreqs['C'] = seq.count("C")	
	numFreqs['G'] = seq.count("G")	
	numFreqs['T'] = seq.count("T")	
	total = numFreqs['A'] + numFreqs['T'] + numFreqs['G'] + numFreqs['C']
	for char in "ACGT":
		numFreqs[char] = numFreqs[char] / total	
	return numFreqs

def diNucFreq(fileName):
	numFreqs = {}
	with open(fileName) as fastFile:
		lines = fastFile.read().splitlines()
		del lines[0]
		seq = "".join(lines)
	seq = seq.replace("N", "A")
	for first in "ACGT":
		for second in "ACGT":
			numFreqs[first + second] = seq.count(first + second) / len(seq)	
	return numFreqs

if __name__ == "__main__":
	fileName = "lambda.fasta"
	if len(sys.argv) == 2:
		fileName = str(sys.argv[1])
	print("Nucleotide Frequences:")
	for key, val in nucFreq(fileName).items():
		print("\t" + str(key) + ":", str(val)) 
	print("Dinucleotide Frequencies:")
	for key, val in diNucFreq(fileName).items():
		print("\t" + str(key) + ":", str(val)) 
