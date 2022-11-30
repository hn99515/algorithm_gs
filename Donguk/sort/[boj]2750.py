N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

for i in range(len(arr)-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for k in arr:
    print(k)

    