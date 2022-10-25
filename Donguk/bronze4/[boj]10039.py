res = 0
for _ in range(5):
    score = int(input())

    if score >= 40:
        res += score
    else:
        res += 40

print(res // 5)