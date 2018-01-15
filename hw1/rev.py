#!/usr/local/bin/python3

import sys

def reverseComplement(fileName = "lambda.fasta"):
	"""Reverse Complement 'filename' which is assumed to be a fasta
		 file. The default is lambda.fasta. Saves the result as
		 fileName.rev.fasta without the original .fasta extension.
	"""
	newSequence = ""
	with open(fileName, "r") as fastFile:
		with open(fileName.split(".")[0] + ".rev.fasta", "w+") as revFile:	
			for line in fastFile:
				if line[0] != ">":
					for char in line:
						if char == "A" or char == "T":
							newSequence = ("A" if char == "T"  else "T") + newSequence
						elif char == "G" or char == "C":
							newSequence = ("G" if char == "C"  else "C") + newSequence
						else: continue
				else:	
					first = line.split(" ")
					first[0] = ">reversed"
					revFile.write(" ".join(first))
			for i in range(0, len(newSequence), 70):
				revFile.write(newSequence[i: i+70] + "\n")
			revFile.write("\n")
				
if __name__ == "__main__":	
	if len(sys.argv) == 2:
		reverseComplement(str(sys.argv[1]))	
	else: 
		reverseComplement()
