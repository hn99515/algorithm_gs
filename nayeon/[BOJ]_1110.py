n = int(input())
new = n # 할당 (n은 변하지않음 immutable data)
new_list = []
cnt = 0
while True:
    if n in new_list:
        break

    left = new % 10

    right = new // 10 + new % 10

    if right >= 10:
        right = right % 10

    new = int(str(left) + str(right))
    new_list.append(new)

    cnt += 1

print(cnt)