# 기지국

import sys
sys.stdin = open('input_11671.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    station = {'A': 1, 'B': 2, 'C': 3}

    for i in range(n):
        for j in range(n):
            if arr[i][j] in station.keys():  # 딕셔너리의 키 값 중에 있다면
                s = station[arr[i][j]]

                for dx, dy in delta:
                    for k in range(1, s+1):  # <- 이 방법 기억하기!
                        nx, ny = i + dx * k, j + dy * k

                        # 범위 안에 위치하는 동안
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'

        # 기지국으로 커버되지 않는 집 수 count
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 'H':
                    cnt += 1

    print(f'#{tc} {cnt}')
