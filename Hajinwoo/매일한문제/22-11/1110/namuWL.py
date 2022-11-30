import sys
sys.stdin = open('input.txt')

# 마지막으로 자른 사람(N을 1이나 0으로 만든 사람)이 승자.
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    res = 'Alice'
    # cnt = 0
    # while 1:
    #     if N <= 1:
    #         break
    #     cnt += 1
    #     if N % 2 == 0:
    #         N = N // 2
    #     else:
    #         N = N // 2 + 1
    # if cnt % 2 == 0:
    #     res = 'Bob'
    if N % 2 != 0:
        res = 'Bob'

    print(f'#{tc} {res}')