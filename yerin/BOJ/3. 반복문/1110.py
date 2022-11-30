count = 0
N = int(input())
n1 = N

while True:
    a = n1 // 10
    b = n1 % 10
    n1 = (b * 10) + ((a + b) % 10)
    count += 1
    if N == n1:
        break

print(count)

#while True:
#    if A < 10:
#        C = A * 11
#    else:
#        B = (A // 10) + (A % 10)
#        C = (A % 10) * 10 + (B % 10)
#    if A == C:
#        break
#    else:
#        A = C
#        count += 1
#print(count)