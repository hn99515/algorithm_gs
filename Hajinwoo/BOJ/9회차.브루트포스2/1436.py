n = int(input())
cnt = 0
NOE = 666                   # 가장 작은 악마의 수
while 1:
    if '666' in str(NOE):   # NOE를 문자열로 바꿨을 때 3개 이상의 6이 포함되어 있다면
        cnt += 1
    if cnt == n:
        print(str(NOE))
        break               # break 안 해주면 while 1이라서 계속 돈다.
    NOE += 1                # while 계속 돌리면서 cnt == n이 될 때까지 1씩 계속 더해준다.