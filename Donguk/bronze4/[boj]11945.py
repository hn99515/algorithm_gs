N, M = map(int, input().split())
for _ in range(N):
    arr = list(map(int, input()))

    for i in range(M//2):
        arr[i], arr[-1-i] = arr[-1-i], arr[i]

    for j in arr:
        print(j, end='')
    print()


