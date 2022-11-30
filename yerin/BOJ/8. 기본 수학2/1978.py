# 소수 찾기

# 소수 : 1과 자기 자신으로 나눌 때만 나누어 떨어지는 자연수

n = int(input())  # 수의 개수
numbers = map(int, input().split())

sosu = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)