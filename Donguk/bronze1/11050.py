n, k = map(int, input().split())

res = 1
for i in range(n, 0, -1):
    res *= i

div = 1
for j in range(k, 0, -1):
    div *= j

div2 = 1
for h in range(n-k, 0, -1):
    div2 *= h

print(int(res / (div*div2)))
