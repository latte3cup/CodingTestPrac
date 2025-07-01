from collections import deque

def hide_and_seek(N, K):
    max_pos = 100001  # 0부터 100000까지
    visited = [0] * max_pos

    queue = deque()
    queue.append(N)

    while queue:
        current = queue.popleft()

        if current == K:
            return visited[current]

        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < max_pos and visited[next_pos] == 0:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

# 입력 처리
N, K = map(int, input().split())
print(hide_and_seek(N, K))