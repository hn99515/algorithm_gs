# 홀수번째는 분모 오름차순, 짝수번째는 분모 내림차순,
# 홀수번째 분자는 내림차순, 짝수번째 분자는 오름차순
# n번째 줄 = n까지 오름차순 내림차순
x = int(input())

n = 0
cnt = 0
while x > cnt:
    n += 1
    cnt += n
cnt -= n
if n % 2 == 0: #  짝수
    a = x - cnt
    b = n - a + 1
else:          #  홀수
    a = n - (x - cnt) + 1
    b = x - cnt

print(f'{a}/{b}')  # a = 분자, b = 분모