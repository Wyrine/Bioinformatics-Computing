#!/usr/local/bin/python3

import sys

def reverseComplement(fileName):
	"""Reverse Complement 'filename' which is assumed to be a fasta
		 file. Converts the first line into ">reversed" + the rest of
		 the contents that were already present on that line. This method
		 returns two items, the first is the first line as a string and
		 the second is a string that contains the reverse complemented
		 sequence with no delimiters or special characters.
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
	fileName = "lambda.fasta"
	DEFAULT_LINE_LEN = 70	
	if len(sys.argv) == 2:
		fileName = str(sys.argv[1])
	
	firstLine, RCSequence = reverseComplement(fileName)
	with open(fileName.split(".")[0] + ".rev.fasta", "w+") as revFile:	
		revFile.write(" ".join(firstLine))
		
		for i in range(0, len(RCSequence), DEFAULT_LINE_LEN):
			revFile.write(RCSequence[i: i+DEFAULT_LINE_LEN] + "\n")
		revFile.write("\n")	
