'''
그래프를 탐색한 결과를 dfs와 bfs 로 나타내자.
방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
더 이상 방문할 수 있는 정점이 없는 경우 종료
정점 번호는 1번부터 N번까지
'''
def dfs(V):         # V - 시작 정점
        print(V, end=' ')
        visited[V] = 1
        for w in adjList[V]:
            # 방문하지 않은 w
            if visited[w] == 0:
                dfs(w)


def bfs(V):                 # V - 시작 정점
    visited = [0] * (N+1)   # visited 생성
    q = []                  # 큐 생성
    q.append(V)             # 시작점 인큐
    visited[V] = 1          # 시작점 처리 표시
    while q:                        # 큐가 비어있으면 종료
        V = q.pop(0)
        print(V, end=' ')                    # visit(v) - 문제에서 주어진 일을 처리
        for w in adjList[V]:        # 인접하고 미방문한 정점 w가 있는 경우 q에 추가
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[V] + 1


N, M, V = map(int, input().split())     # N = 정점의 개수, M = 간선의 개수, V = 탐색 시작 번호
# 인접 리스트 생성한 후 input data 를 삽입
adjList = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

# 인접 리스트 정렬해야만 오름차순으로 출력 가능
for adj in adjList:
    adj.sort()

visited = [0] * (N+1)       # 방문 리스트 생성
dfs(V)
print()
bfs(V)
