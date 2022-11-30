# 단지번호붙이기

# n의 개수, arr, visited 정의
n = int(input())

arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 상하좌우 이동 설정
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# DFS 정의
def DFS(x, y):
    global cnt   # cnt를 사용하기 위해 global 선언
    visited[x][y] = True
    if arr[x][y] == 1:
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and arr[nx][ny] == 1:
                DFS(nx, ny)

cnt = 0
housing = []

# 정의된 DFS를 가지고 arr을 탐색
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == False:
            DFS(i, j)
            housing.append(cnt)
            cnt = 0

# 최종 답 도출
housing.sort()       # 오름차순 정렬
print(len(housing))  # 총 단지수
for i in housing:    # 각 단지내 집의 수
    print(i)