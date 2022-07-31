A = int(input())
B = int(input())
C = int(input())

D = str(A * B * C) # 3개 수를 곱한 후 문자열로 형변환
for i in range(10): # 0~9 까지 순회
    print(D.count(str(i))) # 0부터 순서대로 count
