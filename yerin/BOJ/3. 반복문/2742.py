final = int(input())  # 숫자를 입력받는다

for n in range(final,0,-1):
    print(n)

# range로 줄어드는 숫자를 구현하고 싶다면 위의 3개 구성을 다 써야한다.
# 1까지라서 생략해서 썼더니 SyntaxError가 떴다.
# 역순이라도 범위가 0+1까지니까 주의하자.