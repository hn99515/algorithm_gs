import math
import sys

input = sys.stdin.readline

M,N = map(int, input().split())

def is_prime(num):
    if num == 1:
        return False
        # 제곱근
    sq = int(math.sqrt(num))
    for i in range(2, sq+1):
        if num % i == 0:
            return False

    return True

for i in range(M, N+1):
    if is_prime(i):
        print(i)
