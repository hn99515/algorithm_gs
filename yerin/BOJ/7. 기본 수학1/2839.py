num = int(input())  # 배달해야 하는 설탕 무게

count = 0
while num >= 0:
    if num % 5 == 0:  # 5의 배수인 경우
        count += (num // 5)
        print(count)
        break
    num -= 3
    count += 1  # 5의 배수가 될 때까지 num-3, 봉지+1
else:           # num < 0이면 num이 3kg, 5kg에 정확하게 나눠 떨어지지 않은 것!
    print(-1)

# 구글링의 도움으로 푼 문제..
# num이 3의 배수인 경우에도 if문으로 걸러진다! 이 코드 짠 분 대단..

