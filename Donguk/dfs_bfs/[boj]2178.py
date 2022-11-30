'''
미로 탐색
(1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동
칸을 셀 때에는 시작 위치와 도착 위치도 포함
'''
def bfs(i, j, N):       # i, j 출발위치
    visited = [[0] * M for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        # 미로가 1이면서 도착점에 도착한다면 방문 횟수 표시
        if maze[i][j] == 1:
            if i == N-1 and j == M-1:
                return visited[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 인접한 미로 = 상하좌우
            ni, nj = i + di, j + dj
            # 벽이 아니고 방문하지 않은 곳인 경우 = 0 또는 3
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

sti = 0
stj = 0
print(bfs(sti, stj, N))