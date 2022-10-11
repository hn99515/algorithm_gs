# 정곤이의 단조 증가하는 수

import sys
sys.stdin = open('input_6190.txt')

# 단조 증가하는지 체크
def check(number):
    number_string = str(number)
    for k in range(len(number_string) - 1):
        if number_string[k] > number_string[k+1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))  # N개의 정수

    maxV = 0  # 최대값

    for i in range(N-1):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]

            # 단조 증가한다면 최대값 갱신
            if check(num):
                maxV = max(maxV, num)


    # 최대값이 0이라면 단조증가가 없는 경우 => -1
    if maxV == 0:
        maxV = -1

    print(f'#{tc} {maxV}')