def solution(people, limit):
    p = sorted(people)
    si = 0
    ei = len(people) -1 
    boat = 0
    while si <= ei:
        if si == ei:
            boat+=1
            break
        t = p[si] + p[ei]
        if t <= limit:
            boat+=1
            si+=1
            ei-=1
        else:
            boat+=1
            ei-=1

    return boat