#!/usr/local/bin/python3

import sys
from math import log




if __name__ == "__main__":
	trainingFile = "human_mito.fasta"
	testingFile = "neander_sample.fasta"
	if len(sys.argv) == 3:
		trainingFile = str(sys.argv[1])
		testingFile = str(sys.argv[2])
