#!/usr/local/bin/python3

import numpy as np
import sys

def setupAlign(file1, file2, scoring, alignment):
		"""
        scoring is defined as: 
        scoring[0] = match
        scoring[1] = mismatch
        scoring[2] = gap
		"""
		with open(file1) as f:
				f.readline()
				seq1 = f.read().replace("N", "A").replace("\n", "")
		with open(file2) as f:
				f.readline()
				seq2 = f.read().replace("N", "A").replace("\n", "")
		alignment(seq1, seq2, scoring)
    
def gapFreeAlign_linear(seq1, seq2, scoring):
		#a variable that will have the column score at the end of the iterations
		maxColScore = 0

		#if the length of sequence 1 is longer than that of sequence two, swap them
		if(len(seq1) > len(seq2)): seq1, seq2 = seq2, seq1

		#make an array of len(seq1) initialized with zeros in all elements
		mat = np.zeros(len(seq1), dtype=np.int)
		
		#iterate through 'rows'
		for i in range(len(seq2)):
				#prevElt is the diagonal to compare to
				prevElt = 0
				#update maxColScore
				maxColScore = max(np.max(mat), maxColScore)
				#iterate through the array for that row i
				for j in range(len(seq1)):
						#get left score. if i == 0 then gap + 0 otherwise gap + mat[j-1]
						left = scoring[2] + (0 if j == 0 else mat[j-1])
						#get score from element above. First run this will be gap score + 0
						up = mat[j] + scoring[2]
						#diagonal score is prevElt + (match or mismatch score)
						diag = prevElt + (scoring[0] if seq1[j] == seq2[i] else scoring[1])
						#update this element and the prevElt
						prevElt, mat[j] = mat[j], max(left, up, diag)
		print("Optimal End Gap Free Score:", max(0, np.max(mat), maxColScore))

if __name__ == "__main__":
		scoring = [2, -1, -2]
		f1, f2 = "human_mito.fasta", "neander_sample.fasta"
		if len(sys.argv) > 3:
				scoring  = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
		if len(sys.argv) > 1:
				f1, f2 = str(sys.argv[1]), str(sys.argv[1])
		setupAlign(f1, f2, scoring, gapFreeAlign_linear)
