import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    A = 1
    B = 2
    C = 3
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for k in range(4):
                    for a in range(1, A+1):
                        nx = i + dx[k] * a
                        ny = j + dy[k] * a
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'
            if arr[i][j] == 'B':
                for k in range(4):
                    for b in range(1, B+1):
                        nx = i + dx[k] * b
                        ny = j + dy[k] * b
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'
            if arr[i][j] == 'C':
                for k in range(4):
                    for c in range(1, C+1):
                        nx = i + dx[k] * c
                        ny = j + dy[k] * c
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'
    res = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                res += 1

    print(f'#{tc} {res}')