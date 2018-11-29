from random import randint
from itertools import starmap

def solve(nuts, bolts):
    def q_solve(nuts, bolts, lo, hi):
        if lo >= hi:
            return
        rand_idx = randint(lo, hi)
        #print("lo:", lo, ":hi", hi, ":rand_idx:", rand_idx)
        pivot_idx = partition(bolts, lo, hi, nuts[rand_idx])
        #print("pivot_idx:", pivot_idx, ":val:", bolts[pivot_idx])
        partition(nuts, lo, hi, bolts[pivot_idx])
        q_solve(nuts, bolts, lo, pivot_idx - 1)
        q_solve(nuts, bolts, pivot_idx + 1, hi)
    #hoares partition(3x less swaps than Lomuto)
    def partition(nuts, lo, hi, pivot):
        lt, rt = lo, hi
        while True: 
            #This order of ifs and whiles is very important and cannot be changed
            #First need to check rt first to move pivot to lo
            #then move rt down until beyond all higher, then lt up
            #then finally check lt for pivot, since lt could be at lo
            # and we need to move lt beyond lo and lower 
            if nuts[rt] == pivot:
                nuts[lo], nuts[rt] = nuts[rt], nuts[lo]
                
            while nuts[rt] > pivot and rt > lo:
                rt -= 1
            while nuts[lt] < pivot and lt < hi:
                lt += 1
            if nuts[lt] == pivot:
                nuts[lo], nuts[lt] = nuts[lt], nuts[lo]
                lt += 1
            if lt < rt:
                nuts[lt], nuts[rt] = nuts[rt], nuts[lt]
            else:
                break
        nuts[lo], nuts[rt] = nuts[rt], nuts[lo]
        return rt
        
    q_solve(nuts, bolts, 0, len(nuts) - 1)
    #print(nuts, bolts)
    return list(starmap(lambda i, nut: '%s %s' % (nut, bolts[i]), enumerate(nuts)))
