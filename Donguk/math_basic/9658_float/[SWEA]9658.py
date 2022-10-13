'''
주어진 정수의 앞 두 자리를 유효숫자로 하여 표기하는 프로그램

정수 588235는 5.88235*10^5 인데, 앞의 소수 부분을 소수점 두 번째 자리에서 반올림하여 5.9*105로 나타내는 것
9999 같은 경우 9.999*10^3에서 9.999의 소수점 두 번째 자리를 반올림하여 1.0*104
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = input()

    cnt = 0
    for _ in N:
        cnt += 1
    res = cnt - 1       # res = 10의 제곱승

    num = int(N)
    first_float = num / (10**res)   # 소수점으로 표현
    first_float = round(first_float, 2)     # 소수점 둘째 자리까지 표현

    if first_float > 9:     # 9.999 같은 경우에는 10 * 10^4
        first_float = first_float / 10
        res += 1            # 지수도 +1

    ans = round(first_float, 1)     # 소수점 첫째 자리까지 표현
    print(f'#{tc} {ans}*10^{res}')