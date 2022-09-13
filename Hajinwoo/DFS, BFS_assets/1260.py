import sys
from collections import deque
sys.stdin = open('input.txt')

def dfs(start):
    print(start,end=' ')
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            visited[i]=True
    return visited

def bfs(start):
    q=deque([start])
    visited[start]=True
    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
    return visited

N, M, V = map(int, input().split())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
for i in range(len(graph)):
    graph[i].sort()
print(graph)
dfs(V)
visited = [False]*(N + 1)
print()
bfs(V)