#!/usr/local/bin/python3

import sys

with open(sys.argv[1]) as f:
		total = 1
		longestLen = 0
		curLen = 0
		sumLen = 0
		for line in f:
				if "##" in line:
						total += 1
						if curLen > longestLen:
								longestLen = curLen
						sumLen += curLen
						curLen = 0
				else:
						curLen += len(line.strip('\n \t'))

		print("Average: %f\nLongest: %d\nTotal:%d" % (sumLen/total, longestLen, total))
