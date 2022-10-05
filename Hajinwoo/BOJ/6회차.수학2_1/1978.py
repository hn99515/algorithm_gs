N = int(input())
x = map(int, input().split())
res = 0
for z in x:
    cnt = 0
    if z > 1:
        for y in range(2, z):
            if z % y == 0: # y로 나누어 떨어지면 소수가 아님.
                cnt += 1 # 소수가 아닌 경우 1 증가
        if cnt == 0: # 소수일 경우
            res += 1 # 소수인 경우 1 증가
print(res)