import sys
sys.stdin = open('input.txt')

T = int(input())

lst = []
for _ in range(T):

    w, h = map(int,input().split())
    lst.append((w,h))


for i in lst:
    cnt = 0
    for j in lst:
        if j != i:
            if i[0] < j[0] and i[1] < j[1]:
                cnt += 1
    print(cnt+1, end=' ')
