def solution2(number, k):
    for i in range(k):
        ans=0
        l = len(number)
        for j in range(l):
            check = number[:j] + number[j+1:]
            ans = max(int(check),ans)
        number = str(ans)

    return str(ans)


def solution(number,k):
    number = list(number)
    stack = []
    cur = 0
    while k!=0 and cur < len(number):
        if not stack:
            stack.append(number[cur])
            cur+=1
        elif stack and stack[-1] >= number[cur]:
            stack.append(number[cur])
            cur+=1
        elif stack and stack[-1] < number[cur]:
            stack.pop()
            k-=1
            continue
            
    for i in range(cur,len(number)):
        stack.append(number[i])
    
    for j in range(k):
        stack.pop()
    
    return ''.join(stack)


        
