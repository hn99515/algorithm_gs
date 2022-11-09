import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

for i in num:
    if i in arr:
        print('1')
    else:
        print('0')