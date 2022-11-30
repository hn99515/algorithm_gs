# 순열 사이클
# 런타임에러 발생

def dfs(now):
    i = graph[now]
    if not visited[i]:
        visited[i] = True
        dfs(i)


for _ in range(int(input())):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            result += 1

    print(result)