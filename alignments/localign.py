#!/usr/local/bin/python3

import numpy as np
from globalign import setupAlign, printTraceBack
import sys

def localAlign(seq1, seq2, scoring):
    #tb is traceback matrix
    tb = np.zeros( (len(seq1) + 1, len(seq2)+1) , dtype=np.int ) 
    #mat is the scores matrix
    mat = np.zeros( (len(seq1) + 1, len(seq2)+1), dtype=np.int )

    x, y, maxVal = 0, 0, 0
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            
            #left up and diag are the three cases and thus represent the scores for each
            left = mat[i, j-1] + scoring[2]
            up = mat[i-1, j] + scoring[2]
            diag = mat[i-1, j-1] + (scoring[0] if seq1[i-1] == seq2[j-1] else scoring[1])

            #Which one gives the best score?
            if left >= up and left >= diag and left > 0:
                tb[i,j] = 0 #0 is left as traceback
                #best score is a gap from left
                mat[i, j] = left
            elif up >= left and up >= diag and up > 0:
                tb[i, j] = 1 #1 is up as traceback
                #best score is a gap from up
                mat[i, j] = up
            elif diag >= left and diag >= up and diag > 0:
                tb[i, j] = 2 #2 is diagonal as traceback
                #best score is match/mismatch from diagonal
                mat[i, j] = diag
            else:
                tb[i, j] = 2
            if maxVal < mat[i, j]:
                x, y = i, j
                maxVal = mat[i, j]
    #return tb matrix, the matrix of scores, and a list of tuples of max score
    return tb, mat, [(x, y)]

if __name__ == "__main__":
    scoring = [2, -1, -2]
    f1, f2 = "human.fasta", "fruit_fly.fasta"
    if len(sys.argv) > 3:
         scoring  = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
    if len(sys.argv) > 1:
        f1, f2 = str(sys.argv[1]), str(sys.argv[1])
    tb, mat, indexList, seq1, seq2 = setupAlign(f1, f2, scoring, localAlign)
    print("Optimal Local Alignment:", mat[indexList[0]])
    printTraceBack(seq1, seq2, tb, indexList)
    
