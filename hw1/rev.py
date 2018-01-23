#!/usr/local/bin/python3

#Kirolos Shahat
#rev.py -- Reverse complement a sequence stored in a fasta file

import sys

def reverseComplement(fileName):
	"""Reverse Complement 'filename' which is assumed to be a fasta
		 file. Converts the first line into ">reversed" + the rest of
		 the contents that were already present on that line. This method
		 returns two items, the first is the first line as a string and
		 the second is a string that contains the reverse complemented
		 sequence with no delimiters or special characters.
		 (I found that I could use a translation table to implement it
		 more efficiently but I did not have the time to do so)
	"""
	newSequence = ""
	firstLineVal = []
	with open(fileName, "r") as fastFile:
		for line in fastFile:
			if line[0] != ">":
				for char in line:
					if char == "A" or char == "T" or char == "N":
						newSequence = ("A" if char == "T"  else "T") + newSequence
					elif char == "G" or char == "C":
						newSequence = ("G" if char == "C"  else "C") + newSequence
					else: continue
			else:	
				firstLineVal = line.split(" ")
				firstLineVal[0] = ">reversed"
	return firstLineVal, newSequence
				
if __name__ == "__main__":	
	fileName = "lambda.fasta" if len(sys.argv) < 2 else str(sys.argv[1])
	#default line for fasta file format printing	
	DEFAULT_LINE_LEN = 70	
	
	firstLine, RCSequence = reverseComplement(fileName)
	with open(fileName.split(".")[0] + ".rev.fasta", "w+") as revFile:	
		revFile.write(" ".join(firstLine))
		
		for i in range(0, len(RCSequence), DEFAULT_LINE_LEN):
			revFile.write(RCSequence[i: i+DEFAULT_LINE_LEN] + "\n")
		revFile.write("\n")	
