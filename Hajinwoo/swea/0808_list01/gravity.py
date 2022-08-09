import sys
sys.stdin = open('input1.txt')

N = int(input())

for i in range(N):
    M = int(input())
    # print(M)
    A = list(map(int, input().split()))
    print(A)

    #  낙차에 대한 정의.
    max_v = 0

    for n in range(M):
        cnt = 0
        for m in range(n+1, M):
            if A[n] > A[m]:
                cnt += 1
        if cnt > max_v:
            max_v = cnt

    print(f'#{i+1} {max_v}')