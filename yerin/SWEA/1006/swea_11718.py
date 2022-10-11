# 사냥꾼

import sys
sys.stdin = open('input_11718.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 0: 빈공간 / 1: 사냥꾼 / 2: 토끼 / 3: 바위

    
