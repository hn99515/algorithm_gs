# 1~10000 까지의 숫자 중 셀프 넘버 찾기
# 셀프 넘버의 반대인 생성자가 있는 수는 모으자
# 최종적으로 전체 범위에서 생성자가 있는 수를 제외


def selfNumber():
    natural_n = set(range(1, 10001))            # 1~10000까지의 수를 담은 set (for 집합 연산)
    generate_n = set()                          # 생성자가 있는 수를 모을 set 자료형 (for 중복 제거)
    
    for i in range(1, 10001):                   # 1~10000 까지 순회
        for j in str(i):                        # 문자열로 변환하여 순회
            i += int(j)                         # 생성자가 있는 수를 찾기위해 더한다.
        generate_n.add(i)                       # 생성자가 있는 수를 담기

        self_number = natural_n - generate_n    # 셀프 숫자 = 전체 - 생성자가 있는 수
        sn = sorted(self_number)                # 오름차순 정렬
    
    for i in sn:                                # 집합을 순회 (for 한 줄 출력)
        print(i)
    

selfNumber()