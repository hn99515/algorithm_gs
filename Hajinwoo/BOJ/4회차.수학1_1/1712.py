a = list(map(int, input().split()))

if a[1] >= a[2]: # a[1]이 a[2]보다 크면 애초에 이득 x
    print(-1)
else:
    print(int(a[0]/(a[2]-a[1])+1))