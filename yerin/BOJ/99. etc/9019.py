# DSLR
# 시간초과


import sys
from collections import deque


def bfs():
    queue = deque([(first, '')])
    visited[first] = 1

    while queue:
        now, cmd = queue.popleft()
        if now == last:
            return cmd

        l_now = len(str(now))

        t = (now * 2) % bound
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'D'))

        t = (now - 1) % bound
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'S'))

        if l_now != 4:
            t = now * 10
        else:
            t, d = divmod(now, 10 ** (l_now - 1))
            t += (d * 10)
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'L'))

        if l_now == 1:
            t = now * 1000
        else:
            t, d = divmod(now, 10)
            t += (d * 1000)
        if not visited[t]:
            visited[t] = 1
            queue.append((t, cmd + 'R'))


testcase = int(sys.stdin.readline())
bound = 10000
for _ in range(testcase):
    first, last = map(int, sys.stdin.readline().split())
    visited = [0] * bound
    print(bfs())