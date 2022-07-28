while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break

    # while문으로만 돌리면 break를 쓰지 않는 이상 계속 돌아가서
    # 런타임 에러 EOFError가 뜨게 된다.