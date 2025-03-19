def solution(n):
    if n == 0:
        return 0  # 0의 약수는 0

    answer = 0
    for i in range(1, int(n ** 0.5) + 1):  # 1부터 √n까지 반복
        if n % i == 0: 
            answer += i  
            if i != n // i:  
                answer += n // i  

    return answer
