def solution(arr1, arr2):
    
    return [[x+y for x,y in zip(row_a,row_b)] for row_a,row_b in zip(arr1,arr2)]