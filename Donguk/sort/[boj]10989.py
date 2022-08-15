N = int(input())

arr = []
n = len(arr)
for _ in range(N):
    arr.append(int(input()))

cnt = [0] * (n+1)

for i in range(n):
    cnt[arr[i]] += 1



output = [0] * n



