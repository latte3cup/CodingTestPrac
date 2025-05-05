def solution(n, computers):
    visited = [0] * n
    
    def dfs(computer):
        visited[computer] = 1
        for i in range(n):
            if computers[computer][i] == 1 and not visited[i]:
                dfs(i)
                
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count+=1
            
    return count