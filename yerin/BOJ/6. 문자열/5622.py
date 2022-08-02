dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
grandma = input()

ans = 0
for i in range(len(grandma)):
    for j in dial:
        if grandma[i] in j:
            ans += dial.index(j) + 3

print(ans)
