# 준환이의 운동관리

import sys
sys.stdin = open('input_3431.txt')

T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())  # L <= X <= U

    if L <= X <= U:
        print(f'#{tc} {0}')
    elif X > U:
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {L - X}')