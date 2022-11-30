n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]

print(arr)

for i in range(n):
    for j in range(m):
        arr[i][j] += 1
print(arr)

res = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == k+1:
            res.append(i, j)

print(*res)

