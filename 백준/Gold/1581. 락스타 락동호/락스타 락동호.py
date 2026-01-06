import sys
from collections import deque, defaultdict
##sys.stdin = open("1581/input.txt", "r") ### 백준에는 안들감
input = sys.stdin.readline


arr = list(map(int, input().split()))

FF = arr[0]
FS = arr[1]
SF = arr[2]
SS = arr[3]

if FF + FS > 0:
    EX = 1 if FS > SF else 0
    M = min(SF, FS)

    used_FS = M + EX

    ans = M * 2 + EX + FF  
    if used_FS > 0:
        ans += SS          
else:
    ans = SS + (1 if SF > 0 else 0)

print(ans)


## XF must be FX 
## XS must be SX
## if all_songs includes FX , first is FX