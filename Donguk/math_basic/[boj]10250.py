T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())     # 호텔 높이, 층별 객실 수, N번째 예약 손님
    floor = N % H                           # N번째 손님을 호텔 높이로 나눈 나머지 = 층수
    num  = N // H + 1                       # N번째 손님을 호텔 높이로 나눈 몫 + 1 = 호실

    if N % H == 0:                          # 나누어 떨어지는 경우
        floor = H                           # 층은 호텔 높이
        num = num - 1                       # 방은 1호
    print(f'{floor} * 100 + {num}')
    