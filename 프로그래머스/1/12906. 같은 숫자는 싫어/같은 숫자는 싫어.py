def solution(arr):
    rs = [arr[0]]
    for i in arr:
        if i != rs[-1]:
            rs.append(i)

    return rs