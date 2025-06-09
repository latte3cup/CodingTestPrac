n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                count += dfs(nx, ny)
    return count

answers = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            size = dfs(i, j)
            answers.append(size)

answers.sort()
print(len(answers))
for num in answers:
    print(num)