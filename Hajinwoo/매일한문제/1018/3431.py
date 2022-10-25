import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    L, U, X = list(map(int, input().split()))
    res = 0
    if X > U:
        res = -1
    elif X < L:
        res = L - X

    print(f'#{tc} {res}')