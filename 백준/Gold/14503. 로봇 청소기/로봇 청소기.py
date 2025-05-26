N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaned_count = 0

while True:
    # 1. 현재 칸 청소
    if room[r][c] == 0:
        room[r][c] = 2  # 청소된 칸은 2
        cleaned_count += 1

    moved = False

    # 2. 주변 4칸 탐색 (반시계 방향)
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향 회전
        nx, ny = r + dx[d], c + dy[d]
        if room[nx][ny] == 0:
            r, c = nx, ny
            moved = True
            break

    if moved:
        continue

    # 3. 후진 시도
    back = (d + 2) % 4
    r_back, c_back = r + dx[back], c + dy[back]
    if room[r_back][c_back] != 1:  # 벽이 아니라면
        r, c = r_back, c_back
    else:
        break  # 벽이면 작동 종료

print(cleaned_count)