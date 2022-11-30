# 수영장

import sys
sys.stdin = open('input_1952.txt')

T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    expense = [0 for _ in range(13)]

    for i in range(1, 13):
        # 하루, 한달 비교
        expense[i] = min(plan[i] * price[0], price[1]) + expense[i-1]
        # 3개월 이상부터 3달까지 비교
        if i > 2:
            expense[i] = min(expense[i], price[2] + expense[i-3])
    # 1년 비교
    ans = min(expense[12], price[3])
    print(f'#{tc} {ans}')