'''
정사각형 모양의 지도
1은 집이 있는 곳, 0은 집이 없는 곳
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
각 단지에 속하는 집의 수를 구한 후 리스트에 담아주면 len()으로 단지수 출력 가능
'''
def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if apt[i][j] == 1:
            return visited[i][j]

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and apt[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] == visited[i][j] + 1


N = int(input())
apt = [list(map(int, input())) for _ in range(N)]


print(bfs(i, j, N))

