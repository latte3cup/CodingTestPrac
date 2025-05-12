def solution(tickets):
    tickets.sort()  
    visited = [False] * len(tickets)
    answer = []
    found = False  # 첫 경로 찾으면 더 이상 탐색 안 함

    def dfs(path, depth):
        nonlocal found
        if found:
            return

        if depth == len(tickets):
            answer.extend(path)
            found = True
            return

        current = path[-1]
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == current:
                visited[i] = True
                dfs(path + [tickets[i][1]], depth + 1)
                visited[i] = False  # 못찾으면 돌아와서 안간 것으로 체크

    dfs(["ICN"], 0)
    return answer