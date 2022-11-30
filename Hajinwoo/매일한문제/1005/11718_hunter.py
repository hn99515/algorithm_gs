import sys
sys.stdin = open('11718input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                for n in range(8):
                    for k in range(1, N+1):
                        nx = i + dx[n] * k
                        ny = j + dy[n] * k
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 3 or arr[nx][ny] == 1:
                                break
                            elif arr[nx][ny] == 2:
                                arr[nx][ny] = 4
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 4:
                cnt += 1
    print(f'#{tc} {cnt}')