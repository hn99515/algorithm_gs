n, x = map(int, input().split())
lst = list(map(int, input().split()))

for i in lst:
    if i < x:
        print(i, end = ' ')