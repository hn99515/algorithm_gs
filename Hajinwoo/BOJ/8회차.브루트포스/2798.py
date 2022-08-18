t, m = map(int, input().split())
ex = list(map(int, input().split()))
res = 0
for i in range(t):
    for j in range(i + 1, t):
        for k in range(j + 1, t):
            if (ex[i] + ex[j] + ex[k] > m):
                continue
            else:
                res = max(res, ex[i] + ex[j] + ex[k])
print(res)





