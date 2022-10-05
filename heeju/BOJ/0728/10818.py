import sys

n = int(input())


num = list(map(int, sys.stdin.readline().split()))

num.sort()

print(num[0] ,num[-1], end=" ")