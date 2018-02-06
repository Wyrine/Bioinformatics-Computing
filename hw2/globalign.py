#!/usr/local/bin/python3

import numpy as np
import sys


#traceback matrix: tuple{key = tuple(row, col), value = 
# make a dictionary of tuples as the key 
#


#start i = 1, j = 1
#if (m[i-1][j] > m[i-1][j-1]) and ( m[i-1][j] > m[i][j-1] ):
#    tb[(i, j)] = (i-1, j)
#elif (m[i][j-1] > m[i-1][j]) and ( m[i][j-1] > m[i-1][j-1] ):
#    tb[(i, j)] = (i, j-1)
#else:
#    tb[(i, j)] = (i-1, j-1)




if __name__ == "__main__":
    match, misMatch, gap = 2, -1, -2
    f1, f2 = "human.fasta", "fruit_fly.fasta"
    if len(sys.argv) > 3:
         match, misMatch, gap  = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    elif len(sys.argv) > 1:
        f1, f2 = str(sys.argv[1]), str(sys.argv[1])
