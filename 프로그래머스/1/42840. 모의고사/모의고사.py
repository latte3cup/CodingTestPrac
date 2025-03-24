def solution(answers):
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ans = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        if answer == man1[i % len(man1)]:
            ans[0] += 1
        if answer == man2[i % len(man2)]:
            ans[1] += 1
        if answer == man3[i % len(man3)]:
            ans[2] += 1
            
    max_score = max(ans)
    return [i + 1 for i, score in enumerate(ans) if score == max_score]