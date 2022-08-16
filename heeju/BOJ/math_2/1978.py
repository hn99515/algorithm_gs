# 소수 찾기
n = int(input())
num = list(map(int, input().split()))
result = 0

for i in num:
    # 1이면 소수가 아니니까 
    if i == 1:
        continue
    # 나누어 떨어지는 횟수
    cnt = 0
    for j in range(2, i + 1):
        if i % j == 0:
            cnt += 1

    if cnt == 1:
        result += 1

print(result)