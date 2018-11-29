
#findMaxPossibleArea function below.
def findMaxPossibleArea(hts, l, r):
    
    stk = []
    stk.append(0)
    max_val = 0
    hts.append(0)
    for rt_bndry in range(1, len(hts)):
        ht_at_bndry = hts[rt_bndry]
        while stk and ht_at_bndry < hts[stk[-1]]:
            curr_idx = stk.pop()
            print('curr_idx: ', curr_idx, ' :val: ', hts[curr_idx])
            if stk:
                lt_bndry = stk[-1]
                max_val = max(max_val, hts[curr_idx]*(rt_bndry - lt_bndry - 1))
                print('this_max:', hts[curr_idx]*(rt_bndry - lt_bndry -1))
            else:
                max_val = max(max_val, hts[curr_idx]*rt_bndry)
                print('other_max:', hts[curr_idx]*rt_bndry)
            print('max:', max_val)
        stk.append(rt_bndry)
            
    
    return max_val

findMaxPossibleArea([6,2,5,4,5,1,6], 0, 6)

