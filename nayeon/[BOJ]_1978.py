N = int(input())

nums = list(map(int, input().split()))


cnt = 0
for x in nums:
    possible = 0

    div_num = [n for n in range(1,x+1)]

    for i in div_num:
        if x % i == 0:
            possible += 1
    if possible == 2:
        cnt +=1

print(cnt)




