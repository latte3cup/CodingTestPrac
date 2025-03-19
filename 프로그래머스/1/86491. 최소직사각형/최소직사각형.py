def solution(sizes):
    sizes = [sorted(size, reverse=True) for size in sizes]
    w,h = max(sizes, key=lambda x:x[0]*x[1])
    mw = max(sizes,key=lambda x:x[0])[0]
    mh = max(sizes,key=lambda x:x[1])[1]
    
    w,h = max(w,mw), max(h,mh)
    return w*h