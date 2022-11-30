# 농작물 수확하기

import sys
sys.stdin = open('input_2805.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())  # 농장의 크기
    arr = [list(map(int, input())) for _ in range(n)]

    profit = 0
    for i in range(n):
        if i <= n//2:
            for j in range(n//2-i, (n//2-i)+2*i+1):
                profit += arr[i][j]

        else:
            for j in range(i-n//2, n-(i-n//2)):
                profit += arr[i][j]

    # n = 3 /  2 -> 1
    # n = 5 /  3 -> 1~3  4 -> 2
    # n = 7 /  4 -> 1~5  5 -> 2~4  6 -> 3

    print(f'#{tc} {profit}')