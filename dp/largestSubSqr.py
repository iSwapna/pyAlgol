def  largest_sub_square_matrix(rows, cols, mtx):
    res = 0
    dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            if mtx[i-1][j-1] == 1:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                res = max(res,dp[i][j])
                
    return res
