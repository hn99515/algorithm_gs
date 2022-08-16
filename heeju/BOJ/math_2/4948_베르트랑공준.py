import sys
import math


# 소수인지 확인
def is_prime(x):
    if x == 1:
        return False
    for k in range(2, int(math.sqrt(x))+1):
        if x % k == 0:
            return False
    return True



# 반복문을 통해 케이스를 확인
while True:
    n = int(sys.stdin.readline())
    cnt = 0

    # 범위 내에서 가능한 모든 수가 소수인지 확인
    prime_nums = []
    for i in range(n+1, 2 * n + 1):
        if is_prime(i):
            prime_nums.append(i)
            cnt +=1

    # 입력받은 수가 0이면 반복을 멈춤
    if n == 0:
        break

    print(cnt)