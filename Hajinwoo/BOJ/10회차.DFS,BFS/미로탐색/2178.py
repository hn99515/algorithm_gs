import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(x, y):
    # 상하좌우 델타 탐색
    dx = [-1, 1, 0, 0,]
    dy = [0, 0, -1, 1,]
    # 디큐 쓸거임.
    queue = deque()
    # 현재 위치 추가.
    queue.append((x,y))
    # 큐 값 전부 순회
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 델타 탐색.
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내에서만 돌게 범위 설정
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            # 0 즉, 벽인 경우 무시
            if arr[nx][ny] == 0:
                continue
            # 1인 경우에 이동하면서 이동한 경로에 +1 카운트
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    # 목적지일 때의 카운트 값
    return arr[N-1][M-1]


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

print(bfs(0, 0))
