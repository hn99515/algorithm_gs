num1 = int(input())
num2 = input()

num3 = num1 * int(num2[-1])
num4 = num1 * int(num2[1])
num5 = num1 * int(num2[0])

print(num3)
print(num4)
print(num5)
print(num3 + 10 * num4 + 100 * num5)