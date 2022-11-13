import sys

n = int(sys.stdin.readline())
# 중복 제거
arr = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

for i in num:
    print(1) if i in arr else print(0)
