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
    tb = [(0,1)]
    
    for t in range(1, len(benchMark)):
        #ftmp[0] = fair, no transition
        #ftmp[1] = loaded, transition
        #tmp1 = 0 if the max is fair->fair, 1 if max is loaded->fair
        ftmp, tmp1 = vitHelper(fair[benchMark[t]], 1 - trans_f, trans_l, a, b)

        #ltmp[0] = loaded, no transition
        #ltmp[1] = fair, transition
        #tmp2 = 0 if the max is loaded->loaded, 1 if max is fair->loaded
        ltmp, tmp2 = vitHelper(loaded[benchMark[t]], 1 - trans_l, trans_f, b, a)
        
        a, b = max(ftmp[0], ltmp[1]), max(ftmp[1], ltmp[0])
        tb.append((tmp1, tmp2))
    print(tb)
    return a, b

def vitHelper(dieProb, trans1, trans2, prev1, prev2):
    rv1 = prev1 * trans1 * dieProb
    rv2 = prev2 * trans1 * dieProb
    return [rv1, rv2], (0 if rv1 >= rv2 else 1) 

if __name__ == "__main__":
    f1, f2 = "file1.txt", "file2.txt"
    if len(sys.argv) == 3:
        f1, f2 = sys.argv[1], sys.argv[2]

    fair, loaded, trans_f, trans_l = fwd.setupCasino()

    with open(f1) as f:
        benchMark = f.read().replace("\n", "").replace(" ", "")
    one = runViterbi(benchMark, fair, loaded, trans_f, trans_l)
    print(one[0] + one[1])

    #with open(f2) as f:
    #    benchMark = f.read().replace("\n", "").replace(" ", "")
    #two = runViterbi(benchMark, fair, loaded, trans_f, trans_l)
    #print(two[0] + two[1])

