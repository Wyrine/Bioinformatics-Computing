#!/usr/local/bin/python3

import sys
from rev import reverseComplement

def nucFreq(fileName):
	#numFreqs = {"A": 0, "T": 0, "G": 0, "C": 0}
	numFreqs = {}
	with open(fileName) as fastFile:
		lines = fastFile.read().splitlines()
		del lines[0]
		seq = "".join(lines)	
		#for line in fastFile:
		numFreqs['A'] = seq.count("A") + seq.count("N")	
		numFreqs['T'] = seq.count("T")	
		numFreqs['G'] = seq.count("G")	
		numFreqs['C'] = seq.count("C")	
	total = numFreqs['A'] + numFreqs['T'] + numFreqs['G'] + numFreqs['C']
	for char in "ATCG":
		numFreqs[char] = numFreqs[char] / total	
	return numFreqs

def diNucFreq(fileName):
	numFreqs = {}
	with open(fileName) as fastFile:
		lines = fastFile.read().splitlines()
		del lines[0]
		#make a list, every time you read a line delete the first character and append the
		#new elements to the list, and at the end join them all together into a string.
		#then do the calculations
		#also parse out the first line of the file
	return numFreqs

if __name__ == "__main__":
	fileName = "lambda.fasta"
	if len(sys.argv) == 2:
		fileName = str(sys.argv[1])
	print(nucFreq(fileName))
