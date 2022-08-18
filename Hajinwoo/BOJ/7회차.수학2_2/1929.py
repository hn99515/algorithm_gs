def prime_num(max):
    for i in range(2, int(max**0.5)+1): # 핵심부분. 해당 수의 제곱근까지만 나눠보면 된다!
        if max % i == 0:
            return False
    return True

M, N = map(int,input().split())

for sosu in range(M, N+1):
    if prime_num(sosu):
        print(sosu)