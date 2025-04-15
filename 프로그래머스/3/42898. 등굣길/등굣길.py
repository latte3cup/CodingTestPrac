def solution(m, n, puddles):
    
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    mines = set((y-1,x-1) for x,y in puddles)
    
    for y in range(n):
        for x in range(m):
            if (y,x) in mines:
                dp[y][x] = 0
                continue
                
                
            if y >0:
                dp[y][x] = dp[y][x] + dp[y-1][x]
            if x>0:
                dp[y][x] = dp[y][x] + dp[y][x-1]
                
    return dp[-1][-1] % 1000000007