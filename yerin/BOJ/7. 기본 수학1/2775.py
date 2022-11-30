# k층 n호 거주민 수 = [k층 n-1호] + [k-1층 n호]
# k층 n호 거주민 수 = [k-1층 1호] + ... + [k-1층 n호]

# 호    : 1호 |  2호  |     3호   |
# k-1층 : 1명 |  a명  |     b명   |
# k층   : 1명 | 1+a명 | (1+a)+b명 |  

t = int(input())  # test case 수

for i in range(t):
    k = int(input())  # 층
    n = int(input())  # 호
    floor0 = [f for f in range(1, n+1)]  # 0층 list
    for j in range(k):                   # 1 ~ k층까지 반복
        for m in range(1, n):            # floor0 list의 인덱스로 사용
            floor0[m] += floor0[m-1]     # 층별 각 호실의 사람 수 변경 / [k층 n호] = [k-1층 n호] + [k층 n-1호]
    print(floor0[-1])                    # 가장 마지막 수 출력
        
        
# 1시간 동안 고민했지만 코드를 작성하지 못했다.
# 종이에 적어가며 규칙을 찾았지만 코드로 구현하는데에 어려움이 있었다.
# 공부가 더 필요하다..
    

