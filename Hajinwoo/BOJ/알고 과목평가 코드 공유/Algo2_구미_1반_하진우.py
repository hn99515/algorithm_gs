# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    ex = [list(map(int, input().split())) for __ in range(3)]
    cnt = 0
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            for m in range(1):
                for n in range(1):
                    if ex[m][n] == arr[i][j] and ex[m+1][n+1] == arr[i+1][j+1] and ex[m+2][n+2] == arr[i+2][j+2] and ex[m][n+1] == arr[i][j+1] and ex[m][n+2] == arr[i][j+2] and ex[m+1][n] == arr[i+1][j] and ex[m+1][n+2] == arr[i+1][j+2] and ex[m+2][n] == arr[i+2][j] and ex[m+2][n+1] == arr[i+2][j+1]:
                        #비교할 케이스가 9개 밖에 안 되니까 직접 비교했습니다.
                        cnt += 1

    print(f'#{tc} {cnt}')
