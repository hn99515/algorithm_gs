# 판매량 = n
# c * n(총수입) = a(고정비용) + b * n(가변비용)
# n = a / (c - b)

a,b,c = map(int,input().split())

if b >= c:  # 가변비용이 노트북 가격보다 같거나 크면
    print(-1)
else:
    print(a//(c-b)+1)