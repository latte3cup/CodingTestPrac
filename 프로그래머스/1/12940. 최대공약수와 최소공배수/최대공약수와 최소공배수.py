def solution(n, m):

    
    import math
    
    return [math.gcd(n,m), m * n // math.gcd(n, m)]