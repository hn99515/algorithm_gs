# n=1, (n)+6, (n+6)+12, 18  24
# 6씩 증가

a = int(input())
x=6
y=0
z=1
list_z = [z,]
while a >=z:
    y += 1
    x += y
    z += x
    list_z.append(z)
    if list_z[y-1] == a:
        print(len(list_z))
    elif list_z[y-1] < a <= list_z[y]:
        print(len(list_z))