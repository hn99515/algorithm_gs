# 베르트랑 공준

# 1) 미리 소수 리스트 만들기
num = []  # 범위 내 소수 저장 리스트
for i in range(2, 246913):  # 2~마지막 소수
    cnt = 0

    for p in range(2, int(i**0.5)+1):
        if i % p == 0:
            cnt += 1
            break
    if cnt == 0:
        num.append(i)

# 2) 소수 갯수 세기
while True:
    n = int(input())
    res = 0

    if n == 0:  # 입력의 마지막이 0이면 break
        break

    for i in num:
        if n < i <= 2*n:
            res += 1

    print(res)



# 틀린 코드
# n = int(input())

# count = 0
# for num in range(n+1, 2*n+1):
#     if num == 1:  # 1은 소수 x
#         continue
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:  # 약수가 존재하는 경우
#             break         # 더 이상 검사할 필요 x
#     else:
#         count += 1
# print(count)