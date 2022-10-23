school = int(input())
pc = int(input())
hak = int(input())
home = int(input())

total = school + pc + hak + home

x = 0
y = 0
if total >= 60:
    x = total // 60
    y = total % 60

print(x)
print(y)
