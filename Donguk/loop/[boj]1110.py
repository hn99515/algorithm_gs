N = int(input())
count = 0

while True:
    one = N % 10 # 나머지 = 일의 자리수
    two = N // 10 # 몫은 = 십의 자리수
    a = one + two
    count += 1
    

