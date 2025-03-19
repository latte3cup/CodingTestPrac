def solution(citations):

    ans = 0
    l = len(citations)
    for i in range(l):
        citi = len([x for x in citations if x>=i+1])  #num 이상으로 인용된 갯수 
        if citi >= i+1 and l-citi <= i+1:
            ans = max(i+1,ans)
    return ans