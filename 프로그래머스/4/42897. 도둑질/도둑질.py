import sys
sys.setrecursionlimit(10**7)

def dp(i, money, memo):
    if i >= len(money):
        return 0
    if i in memo:
        return memo[i]
    
    take = money[i] + max(dp(i + 2, money, memo), dp(i + 3, money, memo))
    skip = dp(i + 1, money, memo)

    memo[i] = max(take, skip)
    return memo[i]

def solution(money):
    return max(dp(0, money[:-1], {}),dp(0, money[1:], {}))