# 테스트케이스 개수가 주어지지 않았을때

while True:
    try:
        a, b = map(int, input().split())

    except:
        break

    print(a + b)