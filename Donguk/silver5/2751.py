import sys

T = int(input())
a = []
for _ in range(1, T+1):
    c = int(sys.stdin.readline())
    a.append(c)

a.sort()
for i in a:
    print(i)