n = int(input())

result = 0 # 총합 변수 생성
for i in range(1, n+1): # 1~n 까지 순회
    result += i # 순회할 때마다 +1

print(result)