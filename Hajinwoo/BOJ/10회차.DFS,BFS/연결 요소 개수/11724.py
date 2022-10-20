import sys
sys.stdin = open('input.txt')

sys.setrecursionlimit(10000)

def DFS(now):
    # 1. 방문표시
    visit[now] = True
    # 2. 그래프 탐색
    for i in arr[now]:
        if not visit[i]:
            DFS(i)

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
# 방문 처리용 리스트
visit = [False] * (N + 1)
for i in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
#[[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

cnt = 0

# 포인트 부분.
for j in range(1, N + 1):
    # 해당 정점을 방문하지 않았을 경우
    if not visit[j]:
        if not arr[i]:
            cnt += 1
            visit[i] = True
        else:
            DFS(j)
            cnt += 1

print(cnt)