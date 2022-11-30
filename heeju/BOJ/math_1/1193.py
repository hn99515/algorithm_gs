'''
분수 찾기

1/1  >> 1/2  2/1  >> 3/1  2/2   1/3  >>   1/4   2/3   3/2  4/1

짝 : 분모 n ---> 1 / 분자 1----> n

홀 : 분모 1 ----> n / 분자 n -----> 1

규칙이 이중으로 잇어서 찾기가 어려웠다. 

'''

# n번째 수 구하기 
n = int(input())


num = 0
num_count = 0

while num_count < n:
    num += 1
    num_count += num

num_count -= num

# 짝수일때 
if num % 2 == 0:
    i = n - num_count
    j = num - i + 1

# 홀수일때 
else:
    i = num - (n - num_count) + 1
    j = n - num_count

print(f"{i}/{j}")