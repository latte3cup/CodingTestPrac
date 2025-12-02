N, M = map(int, input().split())
bad = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    bad[a][b] = True
    bad[b][a] = True

count = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if bad[i][j]:
            continue
        for k in range(j + 1, N + 1):
            if bad[i][k] or bad[j][k]:
                continue
            count += 1

print(count)