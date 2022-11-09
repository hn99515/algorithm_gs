T = int(input())

ans = []
for _ in range(T):
    a, b = input().split()
    ans.append((int(a), b))

ans.sort(key=lambda x: x[0])
for i in ans:
    print(i[0], i[1])