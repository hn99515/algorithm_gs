a,b = 55, 75
c = 60

a += c // 60
b += c % 60

if b > 59:
    b -= 60
    a += 1
if a > 23:
    a -= 24

print(a, b)