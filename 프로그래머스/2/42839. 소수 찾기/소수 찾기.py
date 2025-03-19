def is_prime(num):
    if num ==0 or num ==1:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0: 
            return 0
    return 1

def solution(numbers):
    ans = 0
    from itertools import permutations
    l = {int("".join(x)) for y in range(1,len(numbers)+1) for x in list(permutations(list(numbers), y)) }
    for n in l:
        ans = ans+ is_prime(n)
        
    return ans