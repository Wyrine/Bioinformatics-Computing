#!/usr/local/bin/python3

import sys

def reverseComplement(fileName = "lambda.fasta"):
	"""Reverse Complement 'filename' which is assumed to be a fasta
		 file. The default is lambda.fasta. Saves the result as
		 fileName.rev.fasta.
	"""
	myList = []
	fastFile = open(fileName)
	name = fileName.split(".")
	revFile = open(name[0] + ".rev.fasta", "w+")
	return
	#for line in fastFile:
				
	

if __name__ == "__main__":	
	if len(sys.argv) == 2:
		reverseComplement(str(sys.argv[1]))	
	else: reverseComplement()
