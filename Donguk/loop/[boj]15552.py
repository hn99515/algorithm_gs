import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split()) # input과 동일한 함수지만 처리해야 할 데이터가 많을 때 유리
    print(A+B)