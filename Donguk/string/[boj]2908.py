A, B = input().split() # 상근이 숫자 2개 입력

a = A[::-1]            # 숫자를 뒤집어서 저장
b = B[::-1]

if a > b:              # a가 큰 경우
    print(a)
else:
    print(b)           # b가 큰 경우
