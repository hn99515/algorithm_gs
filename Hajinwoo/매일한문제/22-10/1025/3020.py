import sys
sys.stdin = open('input.txt')

N, H = list(map(int, input().split()))
arr = [int(input()) for i in range(N)]
stalagmite = [0]*(H+1)
stalactite = [0]*(H+1)
for i in range(N):
    if i % 2 == 0:
        stalagmite[arr[i]] += 1
    else:
        stalactite[arr[i]] += 1

for i in range(H - 1, 0, -1):
    stalagmite[i] += stalagmite[i + 1]
    stalactite[i] += stalactite[i + 1]
