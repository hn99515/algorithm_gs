N = int(input())
arr = []

for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort(key=lambda x : (x[1], x[0]))

maxV = 0
cnt = 0
for st, et in arr:
    if st >= maxV:
        cnt += 1
        maxV = et

print(cnt)