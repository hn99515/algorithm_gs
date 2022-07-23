A, B, C = map(int, input().split())
x = (A + B) % C
y = ((A % C) + (B % C)) % C
z = (A * B) % C
k = ((A % C) * (B % C)) % C
print(x)
print(y)
print(z)
print(k)