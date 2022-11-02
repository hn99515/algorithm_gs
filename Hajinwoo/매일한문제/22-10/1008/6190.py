import sys
sys.stdin = open('input.txt')

def f(num):
    M = str(num)
    pre = 0
    for k in M:
        if int(k) >= pre:
            pre = int(k)
        else:
            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    key = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            key.append(arr[i] * arr[j])
    res = 0
    for i in key:
        if f(i):
            res = i
    if res == 0:
        res = -1
    print(f'#{tc} {res}')
