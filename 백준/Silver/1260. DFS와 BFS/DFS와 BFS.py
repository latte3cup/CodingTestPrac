def dfs(v, visited, graph):
    visited[v] = True
    print(v, end=' ')
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v, visited, graph)

def bfs(v, visited, graph):
    queue = [v]
    visited[v] = True
    while queue:
        now = queue.pop(0)
        print(now, end=' ')
        for next_v in graph[now]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

# 입력 처리
n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 순서대로 방문
for i in range(1, n + 1):
    graph[i].sort()

# DFS
visited = [False] * (n + 1)
dfs(start, visited, graph)
print()

# BFS
visited = [False] * (n + 1)
bfs(start, visited, graph)
print()