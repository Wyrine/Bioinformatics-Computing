#!/usr/local/bin/python3

import numpy as np
import sys

def globalAlign(seq1, seq2, scoring):
		#tb is traceback matrix
		tb = np.zeros( (len(seq1) + 1, len(seq2)+1) , dtype=np.int ) 
		tb[:, 0] = np.ones(len(seq1)+1, dtype=np.int)
		tb[0,0] = 0
		#mat is the scores matrix
		mat = np.zeros( (len(seq1) + 1, len(seq2)+1), dtype=np.int )

		#set up the matrix with gap scores in first row and first column
		mat[0] = np.arange(0, scoring[2] * (len(seq2)+1), scoring[2])
		mat[:, 0] = np.arange(0, scoring[2] * (len(seq1) + 1), scoring[2])
		for i in range(1, len(seq1) + 1):
				for j in range(1, len(seq2) + 1):
            
						#left up and diag are the three cases and thus represent the scores for each
						left = mat[i, j-1] + scoring[2]
						up = mat[i-1, j] + scoring[2]
						diag = mat[i-1, j-1] + (scoring[0] if seq1[i-1] == seq2[j-1] else scoring[1])

						#Which one gives the best score?
						if left >= up and left >= diag:
								tb[i,j] = 0 #0 is left as traceback
								#best score is a gap from left
								mat[i, j] = left
						elif up >= left and up >= diag:
								tb[i, j] = 1 #1 is up as traceback
								#best score is a gap from up
								mat[i, j] = up
						else:
								tb[i, j] = 2 #2 is diagonal as traceback
								#best score is match/mismatch from diagonal
								mat[i, j] = diag

		#return tb matrix, the matrix of scores, and a list of tuples of max score
		return tb, mat, [(len(seq1), len(seq2))]
