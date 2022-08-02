n = int(input())
m = list(map(int, input().split()))
a = max(m)
nl = 0
for i in range(n):
    nl += m[i]/a*100
print(nl/n)