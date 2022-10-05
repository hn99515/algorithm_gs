# a+b -4 
while True:
    #try로 사용 / 수가 입력되지 않았을때 반복문이 끝나도록 try / except
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break