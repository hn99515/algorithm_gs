# 미로 탐색

from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 0인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 1인 경우 카운트를 하나씩 해줌 (최단 거리 기록)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]  # n, m 최단거리 return


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))