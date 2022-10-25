num = list(map(int, input().split()))

res = 0
for i in num:
    res += i ** 2

ans = res % 10
print(ans)