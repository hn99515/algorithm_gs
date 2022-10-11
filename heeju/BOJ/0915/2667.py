N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
num = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(N):
    for j in range(N):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])