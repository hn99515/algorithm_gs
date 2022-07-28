import sys
T = int(sys.stdin.readline())

t=1
for t in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)