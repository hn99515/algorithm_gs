# DFS와 BFS

from collections import deque

# n: 정점의 개수, m: 간선의 개수, start: 탐색을 시작할 정점의 번호
n, m, start = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    print(start, end = ' ')
    # 현재 노드와 연결된 다른 노트를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    # 큐(queue) 구현을 위하 deque 라이브러리 사용
    q = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 하나의 원소를 뽑아 출력
        now = q.popleft()
        print(now, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


visited = [False] * (n+1)
dfs(graph, start, visited)
print("")
visited = [False] * (n+1)
bfs(graph, start, visited)