import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    l, r = N // 2, N // 2
    res = []
    for i in range(N):
        for j in range(l, r + 1):
            res.append(arr[i][j])
        if i < N // 2:
            l -= 1
            r += 1
        else:
            l += 1
            r -= 1
    print(f'#{tc} {sum(res)}')