import sys
T = int(sys.stdin.readline())

t=1
x=0
for t in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    x+=1
    print(f"Case #{x}: {a} + {b} = {a+b}")