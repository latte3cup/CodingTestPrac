def solution(citations):
    citations.sort(reverse=True)  # 큰 숫자부터 정렬
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            continue
        return i  # 조건을 만족하지 않는 순간 이전 값을 반환
    return len(citations)  # 모든 논문이 조건을 만족하면 전체 개수 반환
