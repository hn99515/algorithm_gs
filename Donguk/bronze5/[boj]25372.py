T = int(input())
for _ in range(T):
    pw = input()

    cnt = 0
    for n in pw:
        cnt += 1

    if 6 <= cnt <= 9:
        print('yes')
    else:
        print('no')