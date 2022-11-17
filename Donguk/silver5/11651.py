import sys

N = int(sys.stdin.readline())

res = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    res.append((b, a))

ans = sorted(res)
for y, x in ans:
    print(x, y)
