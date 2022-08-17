import sys


T = int(input())
ans = 0
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    if N % H == 0:  # N이 H의 배수 일때는 상황이 다름!
        f = H
        n = N // H
    else:
        f = N % H   # 한 라인을 다돌고 남은 호수 개수 (위로 쌓임)
        n = N // H + 1  # 몇라인까지 가득 찼는지 (1호라인 부터 시작)


    ans = f * 100 + n

    print(ans)