#!/usr/local/bin/python3

import sys

def setupCasino():
    fair, loaded = {}, {}
    for i in range(1, 7):
        fair[str(i)] = 1.0/6
        loaded[str(i)] = 1.0/10
    loaded["6"] = 0.5
    return fair, loaded

def runForward(fName, fair, loaded):
    #assume pr(F) = 1, and pr(L) = 0 for initial state
    with open(fName) as f:
        benchMark = f.read().replace("\n", "")
    transition = 0.05
    pastInstance = [fair[benchMark[0]] * (1-transition) * fair[benchMark[0]]]
    pastInstance.append(fair[benchMark[0]]*transition*fair[benchMark[0]])
    
    for t in range(1, len(benchMark)):
        bVal = benchMark[t]
        fVal = fair[bVal]
        lVal = loaded[bVal]
        

    return

if __name__ == "__main__":
    f1, f2 = "file1.txt", "file2.txt"
    if len(sys.argv) == 3:
        f1, f2 = sys.argv[1], sys.argv[2]
    fair, loaded = setupCasino()
    runForward(f1, fair, loaded)
    runForward(f2, fair, loaded)

