# Gravity

import sys
sys.stdin = open('input_Gravity.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())  # 가로 칸 수
    arr = list(map(int, input().split()))  # 각 자리당 박스 수

    # 박스 높이가 작은경우 낙차 +1 => 자신 보다 작은 박스 수 세기
    max_res = 0
    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                cnt += 1
        if cnt > max_res:
            max_res = cnt

    print(f'#{tc} {max_res}')