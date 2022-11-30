n = int(input())

num = 666

cnt = 1
while True:
    if n == 1:
        break

    num += 1
    temp = str(num)

    if '666' in temp:
        cnt += 1
    if cnt == n:
        break
print(num)