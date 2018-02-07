#!/usr/local/bin/python3

import numpy as np
import sys

def setupAlign(file1, file2, scoring, alignment):
    """ setupAlign opens file1 and file2 which are assumed to be fasta
        files such that it reads the contents excluding the header and
        creates a string of seq1 and seq2 for file1 and file2 respectively
        and passes those sequences along with the scoring method to the
        alignment function

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
    tb, mat, listIndex = alignment(seq1, seq2, scoring)
    return tb, mat, listIndex, seq1, seq2


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

def printTraceBack(seq1, seq2, tb, indexList):
    i, j = indexList[0]
    newSeq1, newSeq2 = "", ""
    while i >= 1 and j >= 1:
        if tb[i, j] == 0:#0 is left
            j -= 1
            newSeq2 = seq2[j] + newSeq2
            newSeq1 = "-" + newSeq1
        elif tb[i, j] == 1: #1 is up
            i -= 1
            newSeq1 = seq1[i] + newSeq1
            newSeq2 = "-" + newSeq2
        else: #2 is diagonal -- works
            i -= 1
            j -= 1
            newSeq1 = seq1[i] + newSeq1
            newSeq2 = seq2[j] + newSeq2
    for i in range(0, len(newSeq1), 50):
        print("Seq1:", newSeq1[i: i+50])
        print("Seq2:", newSeq2[i: i+50])


if __name__ == "__main__":
    scoring = [2, -1, -2]
    f1, f2 = "human.fasta", "fruit_fly.fasta"
    if len(sys.argv) > 3:
         scoring  = [int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])]
    if len(sys.argv) > 1:
        f1, f2 = str(sys.argv[1]), str(sys.argv[1])
    tb, mat, indexList, seq1, seq2 = setupAlign(f1, f2, scoring, globalAlign)
    print("Optimal Score:", mat[len(seq1), len(seq2)])
    printTraceBack(seq1, seq2, tb, indexList)
    
