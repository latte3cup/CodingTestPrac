from collections import deque
def bfs(start, N, graph):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return dist

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

# 도로 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 모든 건물에서 BFS 실행
dist = [[0] * (N + 1)]
for i in range(1, N + 1):
    dist.append(bfs(i, N, graph))

best_cost = float('inf')
ans = (0, 0)

# 두 건물 선택
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        total = 0
        for k in range(1, N + 1):
            d = min(dist[i][k], dist[j][k])
            total += d * 2  # 왕복
        if total < best_cost or (total == best_cost and (i, j) < ans):
            best_cost = total
            ans = (i, j)

print(ans[0], ans[1], best_cost)