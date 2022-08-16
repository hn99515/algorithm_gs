a,b,c = map(int,input().split())



if b < c:
    sold = a / (c-b) + 1
else:
    sold = -1


print(int(sold))

