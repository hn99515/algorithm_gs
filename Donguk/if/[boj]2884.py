H, M = map(int, input().split())

if M >= 45: # 45분 이상일 때
    print(H, M-45)
elif H !=0 and M < 45: # 시간이 0이 아니고 45분 미만일 때
    print(H-1, M+15)
elif H == 0 and M < 45: # 시간이 0이고 45분 미만일 때
    print(23, M+15)