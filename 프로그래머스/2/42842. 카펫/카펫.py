def solution(brown, yellow):
    s = brown+ yellow
    for i in range(3,int(s**0.5) +1):
        if s%i !=0: continue
        elif (i-2)*((s//i) -2) == yellow:
            return sorted([i,(s//i)], reverse=True)
        
    return