def solution(N, number):
    if N == number:
        return 1

    dps = [set() for _ in range(9)]

    for i in range(1, 9):
        dps[i].add(int(str(N) * i))  # 5, 55, 555 ...
        for j in range(1, i):
            for a in dps[j]:
                for b in dps[i - j]:
                    dps[i].add(a + b)
                    dps[i].add(a - b)
                    dps[i].add(a * b)
                    if b != 0:
                        dps[i].add(a // b)
        if number in dps[i]:
            return i

    return -1