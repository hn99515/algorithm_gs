import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]

temp = 0
for i in arr:
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
