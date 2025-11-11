import sys
from collections import deque, defaultdict
#sys.stdin = open("19532/input.txt", "r") ### 백준에는 안들감
input = sys.stdin.readline

# 정수 하나
#n = int(input().strip())
# 여러 개
arr = list(map(int, input().split()))

D = arr[0] * arr[4] - arr[1] * arr[3]
x = (arr[2] * arr[4] - arr[1] * arr[5]) // D
y = (arr[0] * arr[5] - arr[2] * arr[3]) // D


print(x,y)