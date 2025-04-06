def solution(routes):
    routes.sort(key=lambda x: x[1])  # 종료 지점 기준으로 정렬
    cnt = 0
    camera = -30001

    for start, end in routes:
        if camera < start:
            cnt += 1
            camera = end  # 새 카메라 설치 지점

    return cnt