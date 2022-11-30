num1, num2 = input().split()

num1 = int(num1[::-1])  # 역순
num2 = int(num2[::-1])  # 역순

if num1 > num2:
    print(num1)
else:
    print(num2)

# 역순으로 만들 때 [::-1]을 사용하면 쉽게 역순으로 만들 수 있다!