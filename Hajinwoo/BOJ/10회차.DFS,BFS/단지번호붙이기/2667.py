import sys
sys.stdin = open('input.txt')

def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
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

n = int(input())
graph = [list(map(int, input()))for i in range(n)]
num = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])