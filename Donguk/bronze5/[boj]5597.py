res = [int(input()) for _ in range(28)]
cnt = [0] * 30

for i in res:
    cnt[i-1] += 1

for j in range(len(cnt)):
    if cnt[j] == 0:
        print(j+1)
