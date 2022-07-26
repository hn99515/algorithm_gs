A, B = map(int, input().split())
C = int(input())

if B + C > 59:
    A += (B + C) // 60
    B = (B + C) % 60
    if A > 23:
        A = A - 24  # A와 24의 위치를 바꿔놓고 왜 틀렸는지 고민한 1인...
else:
    B += C

print(A, B)