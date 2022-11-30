# 미로1

import sys
sys.stdin = open('input_1226.txt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def maze():
    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if arr[nx][ny] == 3:  # 도착점에 도착했다면
                return 1  # 도달 가능

            if not arr[nx][ny]:
                Q.append((nx, ny))
                arr[nx][ny] = 1
    return 0  # 가능하지 않음


for _ in range(1, 11):
    tc = int(input())  # 테스트 케이스 번호
    arr = [list(map(int, input())) for _ in range(16)]
    Q = [(1, 1)]  # 시작점 넣고 시작
    print(f'#{tc} {maze()}')