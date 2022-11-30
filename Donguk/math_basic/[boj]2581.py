'''
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 소수의 합과 최솟값을 찾는 프로그램
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
'''
M = int(input())
N = int(input())

# 에라토스테네스의 체
check_list = [0] * (N+1)            # N 까지 소수를 미리 확인할 빈 배열
for i in range(2, (N // 2) + 1):
    if check_list[i] == 0:
        for j in range(2*i, N+1, i):
            check_list[j] = 1

# 범위 내 소수 확인
prime_number = []
for i in range(M, N+1):           
    if i >= 2:
        if check_list[i] == 0:
            prime_number.append(i) 

if len(prime_number) > 0:
    print(sum(prime_number))
    print(min(prime_number))
else:
    print('-1')
