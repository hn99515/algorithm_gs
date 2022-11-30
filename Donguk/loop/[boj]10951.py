while True: # 루프 실행 <EOF 문제>
    try:
        A, B = map(int, input().split())
        print(A + B)
    except: # 오류 발생 시 오류 표기 후 브레이크가 정석
        break