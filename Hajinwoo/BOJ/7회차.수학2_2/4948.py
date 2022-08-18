def prime_num(max):
    for i in range(2, int(max**0.5)+1): # 핵심부분. 해당 수의 제곱근까지만 나눠보면 된다!
        if max % i == 0:
            return False
    return True

while 1:
    n = int(input())
    cnt = 0

    for i in range(n+1, 2 * n + 1):
        if prime_num(i):
            cnt += 1

    if n == 0:
        break

    print(cnt)