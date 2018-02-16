#!/usr/local/bin/python3

import sys
import forward as fwd

def runViterbi(benchMark, fair, loaded, trans_f, trans_l):
    #assume pr(F) = 1, and pr(L) = 0 for initial state
    #a is previous fair state, assumed to be set as 1
    a = (1-trans_f) * fair[benchMark[0]]
    #b is previous loaded state, assumed to be set as 0
    b = trans_f*loaded[benchMark[0]]
    #traceback list for viterbi, initialized with one tuple that is 
    # x-coord: 0 := fair->fair, 1 := fair->loaded
    # y-coord: 0 := loaded->loaded, 1 := loaded->fair
    tb = [(0,1)]
    
    for t in range(1, len(benchMark)):
        #computing the two fair probabilities
        fStay = a * (1 - trans_f) * fair[benchMark[t]]
        fLeave = a * trans_f * loaded[benchMark[t]]

        #computing the two loaded probabilities
        lStay = b * (1 - trans_l) * loaded[benchMark[t]]
        lLeave = b * trans_l * fair[benchMark[t]]
        
        #appending the new ordered pair for traceback
        tb.append( (0 if fStay >= lLeave else 1, 0 if lStay >= fLeave else 1) )
        
        #new a, b for current cell
        a, b  = max(fStay, lLeave), max(lStay, fLeave) 

    #by now a and b correspond to fair and unfair states of the last time-step
    vitSeq = ""
    curIndex = 0 if a >= b else 1
    toPrint = "L" if curIndex else "F"

    for ordPair in tb[::-1]:
        vitSeq += toPrint
        if ordPair[curIndex]:
            toPrint = "F" if toPrint == "L" else "L"
            curIndex = 0 if curIndex else 1
    return a, b, vitSeq

def initVit(fName, out):
    with open(f1) as f:
        benchMark = f.read().replace("\n", "").replace(" ", "")
    a, b, seq = runViterbi(benchMark, fair, loaded, trans_f, trans_l)
    with open(out, 'w') as f:
        f.write(str(max(a,b)) + "\n" + seq)
    return 

if __name__ == "__main__":
    f1, f2 = "file1.txt", "file2.txt"
    if len(sys.argv) == 3:
        f1, f2 = sys.argv[1], sys.argv[2]

    fair, loaded, trans_f, trans_l = fwd.setupCasino()

    initVit(f1, "viterbi1.txt")
    initVit(f2, "viterbi2.txt")
