# a+b -7
import sys

n = int(input())
for i in range(1,n+1):
    a,b = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {a+b}')