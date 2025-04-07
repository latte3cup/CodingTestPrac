def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    islands = list(range(n))
    ans = 0
    
    def find(x):
        if islands[x] != x:
            islands[x] = find(islands[x])  # 경로 압축
        return islands[x]
    
    for i1, i2, cost in costs:
        root1 = find(i1)
        root2 = find(i2)
        if root1 != root2:
            islands[root2] = root1  # union
            ans += cost

    return ans