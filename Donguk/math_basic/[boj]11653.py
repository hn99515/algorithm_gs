# for i in range(2, N):
#     if N % i:
#         continue
#     else:
#         print(i)
#         N = N / i

N = int(input())
if N == 1:                  # N이 1인 경우 아무것도 출력 X
    print('')

for i in range(2, N+1):     # 소인수분해는 2 ~ N까지 나눠서 체크 (2, 3 들어가면 값이 안나오기에 N까지!)
    if N % i == 0:          # i는 N의 소인수
        while N % i == 0:   # 오름차순으로 보여줘야 하므로 같은 수로 나눴을 때 0이면 계속 나누기 위해 while 문 사용
            print(i)
            N = N / i       # 나눠야 하는 숫자를 업데이트
    else:                   # i로 나눈 나머지가 생긴 경우
        continue            # 계속 진행