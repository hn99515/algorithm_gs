'''
M이상 N이하의 소수를 모두 출력 (아주 큰 수)
소수 판별 시, 해당 수의 제곱근까지만 나눠보면 알 수 있다. 왜? 약수는 대칭으로 이루어져있기 때문!
'''

M, N = map(int, input().split())

for num in range(M, N+1):
    if num == 1:            # 1은 소수에서 제외
        continue
    for i in range(2, int(num**0.5) + 1):   # 약수는 대칭으로 이루어져 있기 때문에 해당 수의 제곱근까지만 나눠보면 알 수 있다.
        if num % i == 0:
            break
    else:
        print(num)
