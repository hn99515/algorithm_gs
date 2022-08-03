a = list(map(int, input().split()))
for n in range(1, 2100000001):
    x = a[0]+a[1]*n
    y = a[2]*n
    if x < y:
        if n==1:
            print(-1)
            break
        else:
            print(n)
            break        
    else:
        pass