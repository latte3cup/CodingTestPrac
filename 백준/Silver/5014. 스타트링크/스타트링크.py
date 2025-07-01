from collections import deque

def bfs(F, S, G, U, D):
    visited = [False] * (F + 1)  # 1층부터 F층까지
    queue = deque()
    queue.append((S, 0)) 
    visited[S] = True

    while queue:
        current, presses = queue.popleft()

        if current == G:
            return presses

        next_up = current + U
        if U > 0 and next_up <= F and not visited[next_up]:
            visited[next_up] = True
            queue.append((next_up, presses + 1))

        next_down = current - D
        if D > 0 and next_down >= 1 and not visited[next_down]:
            visited[next_down] = True
            queue.append((next_down, presses + 1))

    return "use the stairs"


F, S, G, U, D = map(int, input().split())
print(bfs(F, S, G, U, D))