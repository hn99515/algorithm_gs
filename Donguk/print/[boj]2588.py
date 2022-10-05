a = int(input())
b = input() # 문자열로 받아 인덱싱 하자!

c = int(b) % 10 # 일의 자리를 구하는 방법

print(a * c)
print(a * int(b[1])) # 10의 자리
print(a * int(b[0])) # 100의 자리
print(a * int(b))