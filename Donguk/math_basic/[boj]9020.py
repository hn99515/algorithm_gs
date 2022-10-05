'''
골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 이러한 수를 골드바흐 수라고 한다. 
또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다.
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
'''
# 소수 판별 함수
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True
  
T = int(input())
for tc in range(T):
    n = int(input())
    a, b = n // 2, n // 2               # 찾고자 하는 소수는 절반 나눠서 접근 = 차이가 가장 작은 것부터!
    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a, b)
            break
        else:                           # a는 -1, b는 +1 하면서 하나씩 체크
            a -= 1
            b += 1




