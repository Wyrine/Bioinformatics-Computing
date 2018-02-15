#!/usr/local/bin/python3

import sys
from random import random
import forward as fwd

def genHMM(length, states, transProb):
    """ 
        length := the length of the model to generate 
        states := a list of state probabilites
        transProb := probability of transfer to different state
        return value := string wiith generated sequence of length approxSize
    """
    seq = ""
    #0 is fair state, 1 is loaded
    curState = 0
    while len(seq) < 300:
        curState = 0 if random() <= (1-transProb[curState]) else 1
        seq += makeRoll(states[curState])
    return seq

def makeRoll(state):
    rollVal = random()
    startVal = 0.0
    #to account for the possibiity of getting a 1
    returnVal = "6"
    for i in "123456":
        startVal = startVal + state[  i  ]
        if startVal <= rollVal:
            returnVal = i
    return returnVal

if __name__ == "__main__":
    approxSize, (fair, loaded, trans_f, trans_l) = 300, fwd.setupCasino()

    if len(sys.argv) == 2:
        approxSize = int(sys.argv[1])
    seq = genHMM(approxSize, [fair, loaded], [trans_f, trans_l])
    seqScore = fwd.runForward(seq, fair, loaded, trans_f, trans_l)
    print(seq)
    print(seqScore[0] + seqScore[1])
