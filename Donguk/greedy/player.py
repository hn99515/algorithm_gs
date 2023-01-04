n = int(input())
body_info = []
for _ in range(n):
    height, weight = map(int, input().split())
    body_info.append((height, weight))

body_info.sort(reverse=True)

maxV = 0
cnt = 0
for x, y in body_info:
    if y > maxV:
        maxV = y
        cnt += 1

print(cnt)
