import sys
from collections import deque

# 이동 방향 (나이트 8가지)
dirs = [(2,1),(1,2),(-1,2),(-2,1),
        (-2,-1),(-1,-2),(1,-2),(2,-1)]

def bfs(l, start, target):
    if start == target:
        return 0
    
    visited = [[False]*l for _ in range(l)]
    q = deque([(start[0], start[1], 0)])  # (x, y, 이동횟수)
    visited[start[1]][start[0]] = True
    
    while q:
        x, y, cnt = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
                if (nx, ny) == target:
                    return cnt+1
                visited[ny][nx] = True
                q.append((nx, ny, cnt+1))
    return -1

# 입력 처리
#sys.stdin = open("7562/input.txt", "r") ### 백준에는 안들감
input = sys.stdin.readline
n = int(input().strip())
for _ in range(n):
    l = int(input().strip())
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    print(bfs(l, (sx, sy), (tx, ty)))
