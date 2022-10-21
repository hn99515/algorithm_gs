N = int(input())

res = 1
if N <= 1:
    res = 1
else:
    for i in range(1, N+1):
        res *= i

print(res)