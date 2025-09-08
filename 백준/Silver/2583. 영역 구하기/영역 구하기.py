import sys
from collections import deque, defaultdict
#sys.stdin = open("2583/input.txt", "r") ### 백준에는 안들감
input = sys.stdin.readline

M, N, K = map(int, input().split())
rects = [list(map(int, input().split())) for _ in range(K)]

# 직사각형 색칠
arr = [[0]*N for _ in range(M)]
for rect in rects:
    x1,y1,x2,y2 = rect
    for y in range(y1,y2):
        for x in range(x1,x2):
            arr[y][x] = 1


# bfs 정의
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[0]*N for _ in range(M)]
def bfs (x,y):
    if visited[y][x] or arr[y][x]:
        return 0
    inQueue = deque([(x,y)])
    size = 1
    while inQueue:
        xx,yy = inQueue.popleft()
        visited[yy][xx] = True
        for dx,dy in dirs:
            gx, gy = xx+ dx , yy+dy
            if 0<= gx < N and 0<=gy<M and not visited[gy][gx] and not arr[gy][gx]:
                visited[gy][gx] = True
                inQueue.append((gx,gy))
                size+=1
    return size


# bfs 실행
sizes = []
for y in range(M):
    for x in range(N):
        if arr[y][x] ==0 and not visited[y][x]:
            sizes.append(bfs(x,y)) 
sizes.sort()
print(len(sizes))
print(*sizes)

