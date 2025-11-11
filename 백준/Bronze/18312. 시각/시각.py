import sys
from collections import deque, defaultdict
#sys.stdin = open("18312/input.txt", "r") ### 백준에는 안들감
input = sys.stdin.readline

N, K = map(int, input().split())
K = str(K)

count = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            time_str = f"{h:02}{m:02}{s:02}"
            if K in time_str:
                count += 1

print(count)