
def solution2(absolutes, signs):
    signs = list(map(lambda x : 1 if x else -1, signs))
    ls=[]
    for i in range(0,len(absolutes)):
        ls.append(absolutes[i]*signs[i])
    return   sum(ls)

def solution(absolutes, signs):
    
    return sum(x if y else -x for x,y in zip(absolutes,signs))
