from collections import defaultdict, deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count
    

def solution(n, wires):

    min_diff = n  # 최대 차이는 n이 될 수 있음

    for cut in wires:
        new_wires = wires.copy()
        new_wires.remove(cut)

        graph = defaultdict(list)
        for a, b in new_wires:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n + 1)
        size = bfs(1, graph, visited)  # 하나의 컴포넌트 크기
        other_size = n - size
        diff = abs(size - other_size)

        min_diff = min(min_diff, diff)

    return min_diff
