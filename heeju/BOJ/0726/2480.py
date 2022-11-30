a, b, c = map(int,input().split())

# 세개 다 같은경우
if a == b== c:
    money = 10000+ a*1000
    print(money)
# 2가지 같은경우
elif a==b :
    print(1000+ a*100)
elif b==c :
    print(1000+ b*100)
elif a==c:
    money = 1000+ a*100
    print(money)
# 전부 다른경우 , 큰수로 계산 후 반환        
else:
    max_num= max(a,b,c)
    money = max_num*100
    print(money)