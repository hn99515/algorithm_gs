import sys
N = int(input())

tri_six = '666'

lst = []

for n in range(10000000):
    if tri_six in str(n):
        lst.append(n)
print(lst[N-1])