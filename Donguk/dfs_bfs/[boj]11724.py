'''
방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램
'''
import sys
sys.setrecursionlimit(5000)


def dfs(v):
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, sys.stdin.readline().split())        # 정점의 개수 & 간선의 개수
N = V+1
# 정점별 인접리스트 생성
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)
# print(adjList)

visited = [0] * N
cnt = 0
# 정점을 dfs로 탐색하면서 개수 세기
for i in range(1, N):
    if not visited[i]:
        if not adjList[i]:
            cnt += 1
            visited[i] = 1
        else:
            dfs(i)
            cnt += 1
print(cnt)

