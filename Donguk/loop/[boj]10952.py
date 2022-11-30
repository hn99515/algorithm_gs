while True: # 몇 번 순회할 지 모르기 때문에 while
    A, B = map(int, input().split())
    
    if A == 0 and B == 0: # A와 B가 0이면
        break # while문 종료
    else:
        print(A+B)