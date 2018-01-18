#!/usr/local/bin/python3

import sys


def nucFreq(fileName):
	numFreqs = {"A": 0, "T": 0, "G": 0, "C": 0}
	with open(fileName) as fastFile:
		for line in fastFile:
			numFreqs['A'] += line.count("A")	
			numFreqs['T'] += line.count("T")	
			numFreqs['G'] += line.count("G")	
			numFreqs['C'] += line.count("C")	
	total = numFreqs['A'] + numFreqs['T'] + numFreqs['G'] + numFreqs['C']
	for char in "ATCG":
		numFreqs[char] = numFreqs[char] / total	
	return numFreqs


if __name__ == "__main__":
	fileName = "lambda.fasta"
	if len(sys.argv) == 2:
		fileName = str(sys.argv[1])
	print(nucFreq(fileName))
