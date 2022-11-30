a, b, v = map(int,input().split())

k = 0	# 올라가는 데 걸리는 일수
d = 0	# 올라간 높이

while True:
    k += 1
    if a*k - b*(k-1) >= v:
        break
    
print(k)