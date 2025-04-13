def solution(triangle):

    
    for i in range(len(triangle)-2, -1,-1 ):  # 아래부터 병합
        for ind in range(0,len(triangle[i])):
            triangle[i][ind] += max(triangle[i+1][ind],triangle[i+1][ind+1])
        
    return triangle[0][0]