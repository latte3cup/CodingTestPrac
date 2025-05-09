def solution(begin, target, words):
    if target not in words:
        return 0
    
    from collections import deque
    import string
    stack = deque()
    stack.append((begin,0))
    visited = set()
    
    while stack:
        str,depth = stack.popleft()
        if str == target:
            return depth
        
        str += " "
        l = len(str)
        for i in range(1,l):
            str1 = str[:i]
            str2 = str[i:] 
            for c in string.ascii_lowercase:
                new_str = (str1[:-1]+ c + str2).strip()
                if new_str in words and new_str not in visited:
                    stack.append((new_str,depth+1))
                    visited.add(new_str)
                    
    return 0
