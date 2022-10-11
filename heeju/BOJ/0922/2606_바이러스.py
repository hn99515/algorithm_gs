n = int(input())		# 컴퓨터의 수
m = int(input())		# 연결된 컴퓨터 쌍의 수

# 인접리스트 graph 선언 및 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):							# 연결된 컴퓨터 쌍의 수만큼 반복
    x, y = map(int, input().split())		
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * (n+1)	# 방문처리 : 방문한 컴퓨터 수를 출력해야하므로 visited 에 True/False가 아닌 0/1로 처리

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True

dfs(graph, 1, visited)
print(sum(visited)-1)	# 방문한 컴퓨터 개수 - 1번 컴퓨터