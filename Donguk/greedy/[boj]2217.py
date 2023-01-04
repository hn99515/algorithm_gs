N = int(input())
arr = []

for _ in range(N):
    weight = int(input())
    arr.append(weight)

arr.sort(reverse=True)

for i in range(N):
    arr[i] = arr[i] * (i+1)

print(max(arr))