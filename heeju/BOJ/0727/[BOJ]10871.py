#x 보다 작은수 
n, x = map(int, input().split())

a = list(map(int, input().split()))


for i in range(len(a)):
    if a[i] < x:
        # 옆으로 프린트할때 end = " " 공백으로 바꿔주기
        print(a[i], end= " ")
