# 숫자개수 

a = int(input())
b = int(input())
c = int(input())

total = a*b*c

total_str = list(str(total))

print(total_str)


for i in range(10):
    print(total_str.count(str(i)))
