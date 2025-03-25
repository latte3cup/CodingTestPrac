def solution(left, right):
    cnt = 0
    answer = 0
    while(left<=right):
        print(f"left :{left}")
        for i in range(1, int(left ** 0.5) + 1):  # 1부터 √n까지 반복
            if left % i == 0: 
                cnt += 1  
                if i != left // i:  
                    cnt += 1 
        print(cnt)
        if(cnt%2==0): 
            answer += left
        else:
            answer += (-left)
        cnt =0
        print(answer)
        left+=1
        
        

    return answer