T = int(input())
arr = []
for _ in range(T):
    a, b = map(int, input().split())
    arr.append((a, b))

arr.sort()
for i in range(T):
    print(arr[i][0], arr[i][1])