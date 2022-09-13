'''
정사각형 모양의 지도
1은 집이 있는 곳, 0은 집이 없는 곳
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
각 단지에 속하는 집의 수를 구한 후 리스트에 담아주면 len()으로 단지수 출력 가능
'''
def bfs(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and apt[ni][nj] == 1:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                cnt += 1
    return cnt


N = int(input())
apt = [list(map(int, input())) for _ in range(N)]

ans = []        # 세대수를 모을 리스트

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 아파트 & 방문한적 없는 경우
        if apt[i][j] == 1 and visited[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

