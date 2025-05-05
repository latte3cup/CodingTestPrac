def solution(maps):
    from collections import deque
    xlen = len(maps[0])
    ylen = len(maps)
    if maps[ylen-1][xlen-2] == 0 and maps[ylen-2][xlen-1] == 0:  ## 목적지에 도달 할 수 없는 경우
        return -1
    
    
    visited = [[0]* xlen for _ in range(ylen)]
    visited[0][0] = 1
        
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]
    
    
    queue = deque([(0,0)]) 
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위 내 & 벽이 아니고 & 방문 안했으면
            if 0 <= nx < ylen  and 0 <= ny < xlen and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1  # 거리 업데이트
                queue.append((nx, ny))

    return visited[ylen-1][xlen-1] if visited[ylen-1][xlen-1] != 0 else -1
