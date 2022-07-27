# 빠른 a+b
import sys

T = int(input()) #Test case
for i in range(T):
    # sys.stdin.readline() 사용해줘야 시간초과가 발생하지않는다
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)