chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))

res = [0] * 6
for i in range(6):
    if chess[i] != arr[i]:
        res[i] = chess[i] - arr[i]

print(*res)