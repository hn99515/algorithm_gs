'''
단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수

 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력
'''
import sys
sys.stdin = open('s_input.txt')


def check(num):
    number = str(num)
    for k in range(len(number) - 1):
        if number[k] > number[k+1]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = 0
    for i in range(N-1):
        for j in range(i+1, N):
            number = (arr[i] * arr[j])

            if check(number):
                maxV = max(number, maxV)

    if maxV == 0:
        maxV = -1

    print(f'#{tc} {maxV}')
