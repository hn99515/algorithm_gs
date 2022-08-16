'''
100보다 작은 m에 대해서 m = a*b 라면, a와 b 중 적어도 하나는 100의 제곱근인 10보다 같거나 작아야한다.

따라서 100보다 작은 소수를 찾을 때, 제곱근인 10보다 작은 수의 배수만 검사해도 전수조사가 가능하다.

n의 제곱근까지 하나도 나누어떨어지는 수가 없어야 소수! <에라토스테네스 접근>
'''

def is_prime(n):

    if n == 1:
        return False
    else:
        for i in range(2,int(n**(0.5))+1):
            if n % i == 0:
                return False
        return True



s, e = map(int,input().split())

for n in range(s,e+1):
    if is_prime(n) == True:
        print(n)
