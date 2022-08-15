'''
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성
'''
# 계속된 시간초과로 인해 범위를 제한하고 먼저 소수를 모두 구한다.
primenum = []
for num in range(2, 246913):
    cnt = 0
    for i in range(2, int(num**0.5)+1): # 제곱근까지만 확인
        if num % i == 0:
            cnt += 1
            break

    if cnt == 0:        
        primenum.append(num)

while True:
    n = int(input())
    res = 0
    if n == 0:              # 0인 경우 프로그램 종료
        break
    elif n == 1:            # 1인 경우 1 출력
        print(n)
    else:
        for j in primenum:  # 미리 찾아놓은 소수가 조건에 만족한다면 결과 출력
            if n < j <= 2*n:
                res += 1
        print(res)