def solution(numbers, target):
    
    def dfs(index, sum_branch):
        if index == len(numbers):
            return 1 if sum_branch == target else 0
        return dfs(index+1, sum_branch + numbers[index]) + dfs(index+1, sum_branch - numbers[index])
    return dfs(0,0)