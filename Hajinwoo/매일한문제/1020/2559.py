import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0]

temp = 0
for i in arr:
    temp += i
    prefix.append(temp)

key = []
for i in range(k, n+1):
    key.append(prefix[i] - prefix[i - k])

print(max(key))