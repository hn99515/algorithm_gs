import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    arr = [list(input()) for _ in range(8)]
    res = 'no'
    cnt = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'O':
                cnt += 1

    if cnt == 8:
        for i in range(8):
            for j in range(8):
                for k in range(4):
                    for l in range(8):
                        nx = i + dx[k] * l
                        ny = j + dy[k] * l
                        if 0 <= nx < 8 and 0 <= ny < 8:
                            if arr[i][j] == 'O':
                                if arr[nx][ny] == '.':
                                    res = 'yes'
                                else:
                                    res = 'no'
                                    break
    print(f'#{tc} {res}')