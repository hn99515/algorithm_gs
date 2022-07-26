a,b,c = map(int, input().split())
10000 >= a,b,c >= 2
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)