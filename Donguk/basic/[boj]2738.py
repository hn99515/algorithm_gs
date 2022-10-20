n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(arr[i][j] + arr2[i][j], end=' ')
    print()
