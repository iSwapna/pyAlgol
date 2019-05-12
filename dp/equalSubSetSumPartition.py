rom collections import defaultdict
def equalSubSetSumPartition(arr):
    # Write your code here
    n = len(arr)
    sum_n, sum_p = 0, 0
    i, j = 0, 0
      
    # calculate sum of all elements 
    for i in range(n): 
        if arr[i] < 0:
            sum_n += arr[i] 
        else:
            sum_p += arr[i]
            
    sum = sum_n + sum_p
    if sum % 2 != 0: 
        return []
    
    dp = [defaultdict(int) for _ in range(n)]
    dp[0][arr[0]] = 1
    #print("sum_n:", sum_n, " sum_p:", sum_p)
    for i in range(1, n):
        #print("i:-->", i)
        for val in range(sum_n, sum_p+1):
            
            dp[i][val] = dp[i-1][val]
            if val == arr[i]:
                dp[i][val] = 1
            elif val - arr[i] >= sum_n:
                dp[i][val] = dp[i][val] or dp[i-1][val - arr[i]]
            #print(" val:", val, " dp:", dp[i][val])
                
    req = sum/2
    idx = n-1
    if not dp[idx][req]:
        return []
        
    res = [False for _ in range(n)]
    cnt = 0
    while idx >= 0:
        if idx != 0:
            if dp[idx][req] and not dp[idx-1][req]:
                res[idx] = 1
                cnt += 1
                req -= arr[idx]
                if not req:
                    break
        else:
            res[idx] = 1
            cnt += 1
        idx -= 1
    #special case when arr is [-3,3]
    if cnt == n:
        return []
    else:
        return res

