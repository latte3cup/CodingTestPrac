import sys
sys.setrecursionlimit(10**7)

def dfs(i, money, memo):
    if i >= len(money):
        return 0
    if i in memo:
        return memo[i]
    
    # 현재 집을 턴다고 하면
    take = money[i] + max(dfs(i + 2, money, memo), dfs(i + 3, money, memo))

    # 현재 집을 안 턴다고 하면
    skip = dfs(i + 1, money, memo)

    memo[i] = max(take, skip)
    return memo[i]

def solution(money):
    # 원형 처리: case 1 (0 ~ n-2), case 2 (1 ~ n-1)
    return max(
        dfs(0, money[:-1], {}),  # 첫 집 포함, 마지막 제외
        dfs(0, money[1:], {})   # 첫 집 제외, 마지막 포함
    )