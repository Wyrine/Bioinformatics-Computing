#!/usr/local/bin/python3

import sys
import numpy as np
from globalign import globalAlign

def printTraceBack(seq1, seq2, tb, indexList):
		i, j = indexList[0]
		total = 0
		while i >= 1 and j >= 1:
				#0 is left
				if tb[i, j] == 0: j -= 1
				#1 is up
				elif tb[i, j] == 1: i -= 1
				#2 is diagonal 
				else:
						if seq1[i-1] != seq2[j-1]:
								total += 1
						i -= 1
						j -= 1
		return total 

def setupHamming():
		with open(sys.argv[1]) as f:
				print('1:', f.readline().replace('>', '').replace('\n', ''))
				data = ""
				seqs = []
				for line in f:
						if '>' in line:
								seqs.append(data)
								print(str(len(seqs) + 1) + ':', line.replace('>', '').replace('\n', ''))
								data = ""
						else:
								data += line.replace('\n', '').replace(' ', '')
				seqs.append(data)
		scoring = [2, -1, -2]
		
		hams = np.zeros((len(seqs), len(seqs)), dtype = np.int)
		for i in range(len(seqs)):
				for j in range(i, len(seqs)):
						tb, mat, opt = globalAlign(seqs[i], seqs[j], scoring)
						hams[i, j] = hams[j, i] = printTraceBack(seqs[i], seqs[j], tb, opt)
		return hams

if __name__ == "__main__":
		if len(sys.argv) < 2:
				print("Usage: ./ham.py <seq.fasta>")
				sys.exit(1)
		hams = setupHamming()
		print("\n  " + " ".join([str(i) for i in range(1, len(hams)+1)]))
		for i in range(len(hams)):
				print(str(i+1) + " ", end = "")
				for j in range(len(hams)):
						print(hams[i, j], end=" ")
				print()
