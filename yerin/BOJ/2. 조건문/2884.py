H, M = map(int, input().split())
if M > 44:
    print(H, M-45)
elif H > 0 and M < 45:
    print(H-1, M+15)
else:
    print(23, M+15)

'''
time_H, time_M = input().split()
time_H = int(time_H)
time_M = int(time_M)

if time_H == 0 and time_M < 44:
    time_H = 23
    time_M = 60 - (45 - time_M)
elif time_M < 44:
        time_H -= 1
        time_M = 60 - (45 - time_M)
else:
    time_M -= 45
print(time_H, time_M)
'''
# 처음에 경우의 수를 잘못 판단하여 코드를 제대로 짜지 못햇다.
# 이후 차근차근 다시 구조화한 후 문제를  풀었다.
# map() 함수를 잘 이용하자.