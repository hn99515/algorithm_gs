a, b, c = map(int, input().split())

if a == b == c: # 3개 다 같은 경우
    print(10000 + (a * 1000))
elif a == b or b == c or a == c: # 2개 같은 경우: 2개 중 하나 선택
    if a == b:
        print(1000 + (a * 100))
    elif b == c:
        print(1000 + (b * 100))
    elif a == c:
        print(1000 + (c * 100))
elif a != b != c: # 3개 다 다른 경우: 가장 큰 숫자 고르기
    if a > b and a > c:
        print(a * 100)
    elif b > a and b > c:
        print(b * 100)
    elif c > a and c > b:
        print(c * 100)