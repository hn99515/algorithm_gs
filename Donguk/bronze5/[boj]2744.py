s = input()

ans = ''
for i in s:
    if i.islower():
        ans += i.upper()
    else:
        ans += i.lower()

print(ans)