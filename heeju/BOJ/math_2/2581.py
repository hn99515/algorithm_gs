' 소수'

M = int(input())
N = int(input())

num_list = [i for i in range(M,N+1)]
#가장작은 소수
min_num = 100000000
# 합계
total = 0
for num in num_list:
    if num == 1:
        continue
    # 나누어 떨어지는 횟수
    cnt = 0
    for j in range(2, num + 1):
        if num % j == 0:
            cnt += 1

    # 횟수가 1이면 소수
    if cnt == 1:
        total += num
        if num < min_num:
            min_num = num

# 소수가 없으면 -1
if total == 0:
    print(-1)

else:
    print(total)
    print(min_num)




