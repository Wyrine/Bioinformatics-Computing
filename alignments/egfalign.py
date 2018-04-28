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
    
def gapFreeAlign(seq1, seq2, scoring):
		#mat is the scores matrix
		mat = np.zeros( (len(seq1) + 1, len(seq2)+1), dtype=np.int )

		for i in range(1, len(seq1) + 1):
				for j in range(1, len(seq2) + 1):
						#left up and diag are the three cases and thus represent the scores for each
						left = mat[i, j-1] + scoring[2]
						up = mat[i-1, j] + scoring[2]
						diag = mat[i-1, j-1] + (scoring[0] if seq1[i-1] == seq2[j-1] else scoring[1])
						mat[i,j] = max(left, up, diag)
		print("Optimal End Gap Free Score:", max(np.max(mat[len(seq1), :]) , np.max(mat[:, len(seq2)])))

if __name__ == "__main__":
		scoring = [2, -1, -2]
		f1, f2 = "human_mito.fasta", "neander_sample.fasta"
		if len(sys.argv) > 3:
				scoring  = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
		if len(sys.argv) > 1:
				f1, f2 = str(sys.argv[1]), str(sys.argv[1])
		setupAlign(f1, f2, scoring, gapFreeAlign)
