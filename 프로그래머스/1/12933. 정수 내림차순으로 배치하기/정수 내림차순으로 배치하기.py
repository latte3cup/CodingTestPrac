def solution(n):
    a = list(map(int,str(n)))
    a.sort(reverse=True)
    print(a)
    
    return int("".join(map(str,a)))