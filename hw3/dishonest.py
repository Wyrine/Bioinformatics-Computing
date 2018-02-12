#!/usr/local/bin/python3

import sys
from random import random

def genHMM(approxSize, states, pi, transProb):
    """ 
        approxSize := the length of the model to generate 
        states := a list of state probabilites
        pi := the initial starting probabilites. Does get altered from the
        function call to contain the the individual probabilities at the end
        of the model
        Note: Pi and States must have same length, otherwise behavior
        is undefined.
        transProb := probability of transfer to different state
        return value := string wiith generated sequence of length approxSize
    """
    seq = ""
    #updated with previous max probability index
    maxPriorState = 0
    #non-transition probability for each state
    stayProb = 1 - transProb
    #finding max for start
    for i in range(len(states)):
        if pi[i] > pi[maxPriorState]:
            maxPriorState = i

    for t in range(approxSize):
        seq += str(makeRoll(states[maxPriorState]))

        for i in range(len(pi)):
            pi[i] = 0
        
        

    return

def makeRoll(state):
    rollVal = random()
    startVal = 0
    #to account for the possibiity of getting a 1
    returnVal = len(state)
    for i in range(1, len(state)+1):
        startVal += state[i]
        if startVal <= rollVal:
            returnVal = i
    return returnVal





if __name__ == "__main__":
    approxSize, pi, transProb = 300, [1, 0], 0.05
    if len(sys.argv) > 2:
        pi, transProb = [int(sys.argv[2]), int(sys.argv[3])], \
                                    float(sys.argv[4])
    if len(sys.argv) == 2:
        approxSize = int(sys.argv[1])
    state1Prob, state2Prob = {}, {}
    NumElems = 6
    for k in range(0, NumElems):
        state1Prob[k+1] = 1/NumElems
        state2Prob[k+1] = 1/10
    state2Prob[6] = 1/2
    states = [state1Prob, state2Prob]

    genHMM(approxSize, states, pi, transProb)
