def solution(k, dungeons):
    from itertools import permutations
    alldungeon =  len(dungeons)
    l = list(permutations(dungeons,alldungeon))
    
    ans=[]
    for roots in l:
        kk = k
        ongoing = 0
        for root in roots:
            if root[0] > kk:  #최소 요구 피로도가  현재 피로도보다 높다면
                break
            else:
                kk-=root[1]
                ongoing+=1
        
        ans.append(ongoing)
        
        
    return max(ans)