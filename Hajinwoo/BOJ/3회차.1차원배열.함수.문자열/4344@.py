c = int(input())
a = []
for i in range(c):
    a = map(int, input().split())
    b = sum(a[1:])/a[0]
    cnt = 0
    for i in range(1, a):
        if a[i] > b:
            cnt += 1
    print(f'{cnt/a[0]}%')