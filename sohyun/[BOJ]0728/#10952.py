while True:
    a, b = list(map(int, input().split()))
    if a == b == 0:
        break
    else:
        print(a + b)