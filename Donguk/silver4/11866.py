from collections import deque

n, k = map(int, input().split())
q = deque()
ans = []

for i in range(1, n+1):
    q.append(i)
print('<', end='')

while q:
    for i in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())

for i in range(len(ans) - 1):
    print('%d,'%ans[i], end=' ')
print(ans[-1], end='')
print('>')