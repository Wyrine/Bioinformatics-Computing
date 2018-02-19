#!/usr/local/bin/python3

import sys

def setupCasino(trans_f = 0.05, trans_l = 0.1):
    fair, loaded = {}, {}
    for i in range(1, 7):
        fair[str(i)] = 1.0/6
        loaded[str(i)] = 0.1
    loaded["6"] = 0.5
    return fair, loaded, trans_f, trans_l

def runForward(benchMark, fair, loaded, trans_f, trans_l):
    #assume pr(F) = 1, and pr(L) = 0 for initial state
    #a is previous fair state, assumed to be set as 1
    a = (1-trans_f) * fair[benchMark[0]]
    #b is previous loaded state, assumed to be set as 0
    b = trans_f*loaded[benchMark[0]]
    
    for t in range(1, len(benchMark)):
        fairProb = fair[benchMark[t]]
        loadedProb = loaded[benchMark[t]]
        prevF, prevL = a, b

        # (fair * stay + loaded * transition) * fairProb
        a = (prevF*(1-trans_f) + prevL*trans_l) * fairProb
        # (loaded * stay + fair * transition) * loadedProb
        b = (prevL*(1-trans_l) + prevF*trans_f) * loadedProb
    return a, b

def initAndRunForward(fName):
    fair, loaded, trans_f, trans_l = setupCasino()
    with open(fName) as f:
        benchMark = f.read().replace("\n", "").replace(" ", "")
    endProbs = runForward(benchMark, fair, loaded, trans_f, trans_l)
    print("\t" + fName + " forward score:", endProbs[0] + endProbs[1])

if __name__ == "__main__":
    f1, f2 = "file1.txt", "file2.txt"
    if len(sys.argv) == 3:
        f1, f2 = sys.argv[1], sys.argv[2]

    initAndRunForward(f1)
    initAndRunForward(f2)
