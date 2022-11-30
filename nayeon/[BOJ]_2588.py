a = int(input())
b = int(input())

first = ((a % 10) + ((a % 100)//10)*10 + (a // 100)*100) * (b % 10) 
second = ((a % 10) + ((a % 100)//10)*10 + (a // 100)*100) * ((b % 100)//10)
third = ((a % 10) + ((a % 100)//10)*10 + (a // 100)*100) * (b // 100)
final = a * b

print(first)
print(second)
print(third)
print(final)
