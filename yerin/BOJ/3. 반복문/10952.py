while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A + B)

# while True는 'true 동안'이 아니다.
# 영원히 루프를 뜻한다.