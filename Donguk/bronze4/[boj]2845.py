l, p = map(int, input().split())
news = list(map(int, input().split()))

att = l * p
ans = []
for i in news:
    if i != att:
        ans.append(i - att)
    else:
        ans.append(0)

print(*ans)
