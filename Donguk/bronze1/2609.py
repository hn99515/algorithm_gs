a, b = map(int, input().split())

# 최대공약수 - 뒤에서부터 구하면 시간 아낄 수 있음
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

# 최소공배수
for i in range(max(a, b), (a*b)+1):
    if i % a == 0 and i % b == 0:
        print(i)
        break


# math 활용
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
