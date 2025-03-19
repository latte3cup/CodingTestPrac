def solution(numbers):
    """
    너무 무식한 방법
    #from itertools import permutations
    #return max(["".join(map(str, x)) for x in list(permutations(numbers,len(numbers)))])
    """

    
    answer = ''
    numbers = list(map(str, numbers))    
    numbers.sort(key = lambda x : x*10, reverse=True)
    answer = str(int("".join(numbers)))    
    
    return answer