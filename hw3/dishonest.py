#!/usr/local/bin/python3

import sys

def genHMM(approxSize, state1Prob, state2Prob, start1, start2):
    """ 
        approxSize := the length of the model to generate 
        state1Prob := the probabilities of each state for state1
        state2Prob := the probabilities of each state for state2
        start1 := the probability of first state being start
        start2 := the probability of second state being start
        return value := TBD
    """
    
    pass

if __name__ == "__main__":
    approxSize, start1, start2 = 300, 1, 0
    if len(sys.argv) > 2:
        start1, start2 = int(sys.argv[2]), int(sys.argv[3])
    if len(sys.argv) == 2:
        approxSize = int(sys.argv[1])
    state1Prob, state2Prob = {}, {}
    NumElems = 6
    for k in range(0, NumElems):
        state1Prob[k+1] = 1/NumElems
        state2Prob[k+1] = 1/10
    state2Prob[6] = 1/2

    genHMM(approxSize, state1Prob, state2Prob, start1, start2)
