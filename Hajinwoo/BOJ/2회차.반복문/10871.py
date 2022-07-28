n, x = map(int, input().split())
a=list(map(int,input().split()))
for i in range(n): # 수열 a를 이루는 n개의 정수
    if a[i] < x:
        print(a[i], end=" ") # 이거 안 해주면 밑으로 답 나옴