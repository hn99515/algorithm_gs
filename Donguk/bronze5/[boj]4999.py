jh = input()
hospital = input()

cnt = 0
for i in jh:
    if i == 'a':
        cnt += 1

cnt2 = 0
for j in hospital:
    if j == 'a':
        cnt2 += 1

if cnt >= cnt2:
    print('go')
else:
    print('no')