# a+b -5

while True :
    a, b = map(int, input().split())
    # 0 들어오면 멈추기 반복문 빠져나오기 
    if a == 0 and b == 0:
        break
    # 0 0 아니면 더해주기
    else:
        print(a+b)




