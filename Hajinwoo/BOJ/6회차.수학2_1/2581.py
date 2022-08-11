def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴

M = int(input())
N = int(input())
a = []
for x in range(M, N+1):
    if is_prime_num(x) == True: # x가 소수라면
        a.append(x) # x로 이루어진 리스트
print(sum(a))
if None in a:
    print(-1)
else:
    print(min(a))