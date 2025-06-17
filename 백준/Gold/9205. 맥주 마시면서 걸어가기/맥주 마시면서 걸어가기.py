def bfs(locations):
    n = len(locations)
    visited = [False] * n
    queue = [0]
    visited[0] = True

    while queue:
        current = queue.pop(0)
        cx, cy = locations[current]
        if current == n - 1:
            return "happy"

        for i in range(n):
            if not visited[i]:
                nx, ny = locations[i]
                dx = abs(cx - nx)
                dy = abs(cy - ny)
                if dx + dy <= 1000:  
                    visited[i] = True
                    queue.append(i)

    return "sad"

t = int(input())
for _ in range(t):
    n = int(input())
    locations = []
    for _ in range(n + 2):
        x, y = map(int, input().split())
        locations.append((x, y))
    print(bfs(locations))