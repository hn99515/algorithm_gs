'''
# 손익분기점
손익분기점 넘는 시점 판매량 갯수 구하기
A는 고정비용 , B는 가변비용 C 는 노트북 가격
n은 노트북 판매 갯수

'''

A, B, C = map(int, input().split())


# 가변 비용이 노트북 1대 가격보다 크면 손익분기점이 생기지않는다
if B >= C:
    print(-1)


# A+B*n = C*n > n = A/(C-B)
else:
    print(int((A/(C-B)+1))) # int로 감싸줘야 소숫점이 나오지않는다
    
