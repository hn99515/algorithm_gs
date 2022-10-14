import sys
sys.stdin = open('input.txt')
'''
바닥이 될 idx 혹은 바닥과 가장 많은 차이를 가진 값 찾으면 되는 문제.
'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        res = max(res, cnt)
    print(f'#{tc} {res}')