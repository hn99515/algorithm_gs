# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

mul = list(str(A * B * C))  
# 세 개의 자연수의 곱을 문자로 리스트에 저장

for i in range(10):
    print(mul.count(str(i)))
# .count()를 활용하여 문자 개수 세기
