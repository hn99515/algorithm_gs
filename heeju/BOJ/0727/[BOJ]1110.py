# 더하기 사이클 
n = int(input())
num = n
# 원래 숫자로 돌아오는 횟수 / 우리가 구하고자하는 값
cnt = 0

while True:
    # ex) 26 > 26//10 = 2
    a = num // 10
     # ex) 26 > 26%10 = 6
    b = num % 10
    #  # ex) (2+6) %10 = 8 
    c = (a+b) % 10
    # 두번째 수 * 10 + 새로 만든 c 
    num = (b*10) + c
    cnt += 1
    # 입력숫자와 같은 숫자가 되면 반복문 빠져나오기 
    if (num == n):
        break
    

print(cnt)
