'''
주어진 수 N 개 중에서 소수가 몇 개인지 찾아서 출력
소수 = 1과 자기 자신만을 약수로 가진 수
'''

N = int(input())
is_prime_num = list(map(int, input().split()))

cnt = 0                         # 소수의 개수 저장
for i in is_prime_num:
    if i != 1:                  # 1은 제외
        for j in range(2, i):   # 2 ~ i-1까지의 숫자를 모두 나누기
            if i % j == 0:      # 나눴을 때 나머지가 0이면 소수가 아님
                break
        else:
            cnt += 1            # for - else

print(cnt)