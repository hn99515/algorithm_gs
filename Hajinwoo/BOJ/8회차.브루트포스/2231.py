N = int(input())
res = []
for i in range(1, N+1):
    A = sum(map(int, list(str(N))))
    A_sum = i + A
    if A_sum == N:
        res.append(N)
        break
print(res)