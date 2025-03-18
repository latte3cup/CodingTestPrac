def solution2(array, commands):
    ans=[]
    for num in range(0,len(commands)):
        i,j,k = commands[num]
        ans.append(sorted(array[i -1:j])[k -1])
    return ans

def solution(array, commands):
     return [sorted(array[command[0] -1:command[1] ])[command[2] -1]
             for command in commands]
             