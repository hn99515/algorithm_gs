M = int(input())
N = int(input())

primenum = []                       # 소수를 담는 리스트
for num in range(M, N+1):           
    cnt = 0                         # 소수와 소수가 아닌 수를 구분하기 위함
    if num > 1:                     # 소수 판별은 1보다 큰 수 부터
        for i in range(2, M+1):     # 2 ~ M 까지 나눠보자
            if num % i == 0:        # 소수가 아니면 cnt +1
                cnt += 1
                break               # 소수가 아닌 수를 계속 체크할 필요 X
        
        if cnt == 0:                
            primenum.append(num)

if len(primenum) > 0:
    print(sum(primenum))
    print(min(primenum))
else:
    print('-1')