#!/usr/local/bin/python3

import sys

def nucFreq(fileName):
	""" compute the frequency of each nucleotide in fileName which
			is assumed to be a fasta file. Returns a dictionary of size 4
	"""
	numFreqs = {}
	with open(fileName) as fastFile:
		fastFile.readline()
		seq = fastFile.read().replace("N", "A").replace("\n", "")
	numFreqs['A'] = seq.count("A") / len(seq) 
	numFreqs['C'] = seq.count("C") / len(seq)
	numFreqs['G'] = seq.count("G") / len(seq)
	numFreqs['T'] = seq.count("T") / len(seq)
	#for char in "ACGT":
	#	numFreqs[char] /= len(seq)
	return numFreqs

def diNucFreq(fileName):
	""" Computes the frequency of each dinucleotide in fileName
			which is assumed to be a fasta file. Returns a dictionary of
			size 16
	"""
	numFreqs = {}
	with open(fileName) as fastFile:
		fastFile.readline()
		seq = fastFile.read().replace("N", "A").replace("\n", "")
	#wanted to use count here as well but it did not give the proper
	#value because "AAA".count("AA") = 1 but it should be 2
	for i in range(0, len(seq) - 1):
		temp = seq[i:i+2]
		if temp not in numFreqs:
			numFreqs[temp] = 0
		numFreqs[temp] += 1
	for key in numFreqs:
		numFreqs[key] /= (len(seq) - 1)
	return numFreqs

if __name__ == "__main__":
	fileName = "lambda.fasta"
	if len(sys.argv) == 2:
		fileName = str(sys.argv[1])
	print("\t Nucleotide Frequences:")
	for key, val in nucFreq(fileName).items():
		print("\t " + str(key) + ":", str(val)) 
	print("\t Dinucleotide Frequencies:")
	diNuc = diNucFreq(fileName)
	for bp1 in "ACGT":
		for bp2 in "ACGT":
			print("\t " + bp1 + bp2 + ":", diNuc[bp1+bp2])
#	for key, val in diNucFreq(fileName).items():
#		print("\t " + str(key) + ":", str(val)) 





