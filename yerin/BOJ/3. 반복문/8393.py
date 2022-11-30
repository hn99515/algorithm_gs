number = int(input())  # 숫자를 입력받는다.

ans = 0  # 누적합을 초기화

# 1부터 number까지 숫자를 더하는 반복문
for n in range(1, number+1):  
    ans += n  

print(ans)

# 1트만에 성공! ><