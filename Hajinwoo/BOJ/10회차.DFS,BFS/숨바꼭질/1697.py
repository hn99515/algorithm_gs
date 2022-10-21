import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        X = q.popleft() # 시작 지점 X = 5
        if X == K:      # 동생 찾으면 break
            print(dist[X])
            break
        for i in (X - 1, X + 1, X * 2):
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = dist[X] + 1
                q.append(i)

N, K = map(int, input().split())
# X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동.
# 힌트 : 5-10-9-18-17 순으로 가면 4초만에 찾을 수 있다.
# BFS를 쓰는 문제.

MAX = 100000
dist = [0] * (MAX + 1)

bfs()