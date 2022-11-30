# 분해합

n = int(input())
min = n
flag = 0
for i in range(1,n):
    sum = i
    tmp = i
    while tmp > 0:
        sum += tmp % 10
        tmp = tmp // 10
    if sum == n:
        flag = 1
        if min > i:
            min = i   

if flag == 1:   
    print(min)
else:
    print(0)

# 다시 풀어볼 문제..