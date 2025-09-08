import sys
from collections import deque, defaultdict
#sys.stdin = open("10026/input.txt", "r") ### 백준에는 안들감
input = sys.stdin.readline

# 정수 하나
n = int(input())
arr_normal = [list(input().strip()) for _ in range(n)]
arr_disabled = [['R' if c == 'G' else c for c in row] for row in arr_normal]
visited_normal = [[0]*n for _ in range(n)]
visited_disabled =[[0]*n for _ in range(n)]


# bfs 정의
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(x,y,arr,visited):
    if visited[y][x]:
        return
    inQueue = deque([(x,y)])
    size = 1
    first_color = arr[y][x]
    while inQueue:
        xx,yy = inQueue.popleft()
        visited[yy][xx] = 1
        for dx,dy in dirs:
            gx,gy = xx+dx,yy+dy
            if 0<=gx<n and 0<=gy<n and not visited[gy][gx] and arr[gy][gx] == first_color:
                inQueue.append((gx,gy))
                visited[gy][gx] = 1
                size+=1
    
    return size

areas_for_normal = []
areas_for_disabled = []
for y in range(n):
    for x in range(n):
        if not visited_normal[y][x]:
            areas_for_normal.append(bfs(x,y,arr_normal,visited_normal))

for y in range(n):
    for x in range(n):
        if not visited_disabled[y][x]:
            areas_for_disabled.append(bfs(x,y,arr_disabled,visited_disabled))

#print(len(areas_for_normal))
#print(len(areas_for_disabled))
ans = [len(areas_for_normal),len(areas_for_disabled)]
print(*ans)
