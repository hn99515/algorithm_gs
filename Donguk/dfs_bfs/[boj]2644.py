"여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성"
from collections import deque

def bfs(num1):
    q = deque()
    q.append(num1)
    visited[num1] = True

    while q:
        v = q.popleft()
        
        for w in adjList[v]:
            if visited[w] == False:
                q.append(w)
                res[w] = res[v] + 1     # 이전 대비 +1
                visited[w] = True


n = int(input())
num1, num2 = map(int, input().split())

m = int(input())
adjList = [[] for _ in range(n+1)]      # 인접리스트 생성
for _ in range(m):
    a, b = map(int, input().split())    # 양방향
    adjList[a].append(b)
    adjList[b].append(a)

# print(adjList)

visited = [False] * (n+1)   # 방문 체크
res = [0] * (n+1)           # 촌수 체크

bfs(num1)
if res[num2] > 0:           # 촌수 확인!
    print(res[num2])
else:
    print(-1)