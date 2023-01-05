N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

cnt = 0
for i in range(N-1, 0, -1):
    if arr[i] <= arr[i-1]:
        cnt += arr[i-1] - arr[i] + 1
        arr[i-1] = arr[i] - 1

print(cnt)