import sys

n, k = map(int, sys.stdin.readline().split())       # N = 온도 측정한 전체 날짜 수 / K = 합을 구하기 위한 연속 날짜 수
arr = [0]+list(map(int, sys.stdin.readline().split()))

prefix = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i]

ans = -10000000
for i in range(k, n):
    ans = max(ans, prefix[i] - prefix[i-k])
    # a, b = map(int, sys.stdin.readline().split())
    # print(prefix[b] - prefix[a - 1])
    print(ans)