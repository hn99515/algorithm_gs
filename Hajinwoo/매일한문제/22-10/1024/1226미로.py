import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    # 미로의 시작점은 항상 1, 1
    q.append((1, 1))
    visit = []
    visit.append((1, 1))
    while q:
        x, y = q.popleft()
        # 델타 탐색
        for k in range(4):
            nx = x + dy[k]
            ny = y + dx[k]
            if nx < 1 or nx >= 15 or ny < 1 or ny >= 15:
                continue
            if arr[nx][ny] == 1 or arr[nx][ny] == 2:
                continue
            if arr[nx][ny] == 3:
                return 1
            arr[nx][ny] = 2
            q.append((nx, ny))
    return 0


for _ in range(2):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    res = bfs()

    print(f'#{tc} {res}')