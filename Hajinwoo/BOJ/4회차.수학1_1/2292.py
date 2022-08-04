# n=1, (n)+6, (n+6)+12, 18  24   z 6의 배수로 증가.
#    6     12     18     24      x
#       6      6     6           

a = int(input())
y=1
z=1
while a > z:
    z += 6 * y  # 6의 배수로 증가
    y += 1      # n 번 증가.
print(y)