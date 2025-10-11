import sys
from collections import deque, defaultdict
##sys.stdin = open("16637/input.txt", "r") ### 백준에는 안들감
input = sys.stdin.readline

def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def dfs(idx, value):
    global max_value
    if idx >= len(op):
        max_value = max(max_value, value)
        return
    
    next_value = calc(value, op[idx], num[idx + 1])
    dfs(idx + 1, next_value)
    
    if idx + 1 < len(op):
        bracket_value = calc(num[idx + 1], op[idx + 1], num[idx + 2])
        next_value = calc(value, op[idx], bracket_value)
        dfs(idx + 2, next_value)

# 입력 처리
N = int(input())
expr = input().strip()

num = []
op = []
for i in range(N):
    if i % 2 == 0:
        num.append(int(expr[i]))
    else:
        op.append(expr[i])

max_value = -2**31
dfs(0, num[0])
print(max_value)