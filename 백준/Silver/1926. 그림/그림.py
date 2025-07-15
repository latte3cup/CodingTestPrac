from collections import deque

n, m = map(int, input().split())

# 도화지 입력 받기
graph = [list(map(int, input().split())) for _ in range(n)]

# 방문 여부 기록
visited = [[False] * m for _ in range(n)]

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    area = 1

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area += 1
    return area

num_pictures = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            num_pictures += 1
            area = bfs(i, j)
            max_area = max(max_area, area)

print(num_pictures)
print(max_area)
