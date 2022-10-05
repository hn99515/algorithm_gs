c = int(input())
a = []
for i in range(c):
    a = a.append(list(map(int, input().split())))
    b = sum(a[1:])/a[0]
    cnt = 0
    for i in range(1, a):
        if a[i] > b:
            cnt += 1
    res = cnt/a[0] * 100
    print(f'{res}%')#res:x.3f