'''
1부터 N까지 정수 N개로 이루어진 순열
       정점 (1, 2, 3, 4, 5, 6, 7, 8)
순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클"
N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램
'''
import sys
sys.setrecursionlimit(2000)


def dfs(v):
    visited[v] = 1
    for w in adjList[v]:
        if visited[w] == 0:
            dfs(w)


T = int(input())
for _ in range(T):
    V = int(input())        # 정점의 개수
    arr = list(map(int, input().split()))

    N = V + 1
    # print(arr)

    adjList = [[] for _ in range(N)]
    for idx, val in enumerate(arr, 1):
        adjList[idx].append(val)
    # print(adjList)

    cnt = 0
    visited = [0] * N
    for i in range(1, N):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(cnt)