#1
n = int(input())
for i in range(10):
    print(f'{n} * {i} =  {n * i}')

#2
t = int(input)
for i in range(t):
    a, b = list(map(int, input().split()))
    print(f'{a} + {b} = {a + b}')

#3
n2 = int(input())
total = 0
for i in range(n2 +1):
    total += i
print(total)

import sys

#4
import sys
t1 = int(sys.stdin.readline())
for i in range(t1):
    c, d = list(map(int, sys.stdin.readline().split()))
    print(c + d)

#5
n3 = int(sys.stdin.readline())
for i in range(1, n3 +1):
    print(i)

#6
n4 = int(sys.stdin.readline())
for i in range(n4, 0, -1):
    print(i)

#7
import sys
t2 = int(sys.stdin.readline())
for i in range(t2):
    e, f = list(map(int, sys.stdin.readline().split()))
    print(f'Case #1: {e + f}')
