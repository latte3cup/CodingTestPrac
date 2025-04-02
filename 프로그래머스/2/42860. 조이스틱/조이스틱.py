def solution(name):
    ord_l = list(map(abs,[ord(c)-65 -26 if ord(c)-65 >13 else ord(c) - 65 for c in name]))
    move_horizontal = sum(ord_l)     # 상하 조작 횟수
    print(ord_l)
    
    # l = []
    # for ind,offset in enumerate(ord_l):
    #     l.append((ind,offset))
    
    #좌우 조작 횟수
    move = len(ord_l) - 1 #A 가 없는 경우 (최대)
    for i in range(len(ord_l)):
        next_right = i+1
        while next_right<len(ord_l) and ord_l[next_right] == 0:
            next_right+=1
        
        move_right_and_to_left = 2* i + len(ord_l) - next_right
        move_left_and_to_right = 2* (len(ord_l) - next_right) + i
        
        move = min(move,move_right_and_to_left,move_left_and_to_right)
        
    return move_horizontal + move