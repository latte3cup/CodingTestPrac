from itertools import permutations

N = int(input())
queries = []

for _ in range(N):
    num, s, b = map(int, input().split())
    queries.append((str(num), s, b))

count = 0

# 1~9까지 숫자로 만든 모든 3자리 순열 (504개)
for perm in permutations('123456789', 3):
    candidate = ''.join(perm)

    ok = True
    for qnum, qs, qb in queries:
        strike = sum(candidate[i] == qnum[i] for i in range(3))
        ball = sum(qnum[i] in candidate for i in range(3)) - strike

        if strike != qs or ball != qb:
            ok = False
            break

    if ok:
        count += 1

print(count)