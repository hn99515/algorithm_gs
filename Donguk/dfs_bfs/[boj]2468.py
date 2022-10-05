'''
많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사
일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태

안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역
어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산
'''
# 최대 높이 찾는 함수
def max_height(N):
    maxV = 0
    for i in range(N):
        for j in range(N):
            if height[i][j] > maxV:
                maxV = height[i][j]
    return maxV


def bfs(i, j, rain):
    q = []
    q.append((i, j))
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        # 인접 = 상하좌우만 성립
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            # 2차원 배열 범위 내 & 높이 > 비의 양 & 방문한 적 없음
            if 0 <= ni < N and 0 <= nj < N and height[ni][nj] > rain and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]

# 비의 양을 (최대값-1)까지 순회
r = max_height(N)
cnt_max = 0         # 안전 영역의 최대 개수
for rain in range(r):
    # 비의 양이 바뀔 때마다 visited 리스트 초기화
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    # 2차원 배열 순회
    for i in range(N):
        for j in range(N):
            # 안전영역 조건 확인
            if height[i][j] > rain and visited[i][j] == 0:
                bfs(i, j, rain)
                cnt += 1
    # 비의 양에 따른 안전 영역 개수 최대치
    if cnt > cnt_max:
        cnt_max = cnt

print(cnt_max)