N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()
for _ in range(M):
    arr[0] += 1
    arr[N-1] -= 1
    arr.sort()

print(arr[N-1]-arr[0])