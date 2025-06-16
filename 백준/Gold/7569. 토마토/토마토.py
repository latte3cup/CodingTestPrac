from collections import deque

# 입력 받기
M, N, H = map(int, input().split())
box = []

for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    box.append(layer)

# 이동 방향: 위, 아래, 앞, 뒤, 왼쪽, 오른쪽
dz = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, -1, 1]

queue = deque()

# 처음부터 익은 토마토들을 전부 큐에 넣는다
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                queue.append((z, y, x))

# BFS 실행
while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]

        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if box[nz][ny][nx] == 0:
                box[nz][ny][nx] = box[z][y][x] + 1
                queue.append((nz, ny, nx))

# 결과 확인
result = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 0:
                print(-1)
                exit()
            result = max(result, box[z][y][x])

# 처음부터 1이었으면 0일, 아니라면 -1 빼기
print(result - 1)