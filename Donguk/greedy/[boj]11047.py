N, K = map(int, input().split())
change = []

for _ in range(N):
    a = int(input())
    change.append(a)

change.sort(reverse=True)

cnt = 0
for money in change:
    if money > K:
        continue
    else:
        cnt += K // money
        K = K % money

print(cnt)