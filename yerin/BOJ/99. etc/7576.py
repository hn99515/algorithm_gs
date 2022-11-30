# 토마토

from collections import deque

m, n = map(int, input().split())  # 가로, 세로
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(m):  # 익은 토마토 큐에 저장
        if graph[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and graph[a][b] == 0:
                queue.append([a, b])
                graph[a][b] = graph[x][y] + 1


bfs()
answ = 0
for i in graph:  # 최단거리를 graph에 다 표시한 후, 0이 존재하면 -1 출력
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answ = max(answ, max(i))  # 0이 존재하지 않으면 최대값 출력
print(answ - 1)   # 처음을 1로 시작했기 때문에 -1 빼기
