import sys
sys.stdin = open('input.txt')
'''
라운드 함수만 기억하고 있으면 IM 축에도 못 드는 문제였음.
if 라운드 없이 푼다고 생각하면:
 함수 새로 써서 반올림해주는 함수 짜면 될듯.
'''
T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = input()
    for i in N:
        cnt += 1
    # N의 갯수 - 1만큼 10의 제곱 해줘야함.
    res = cnt - 1
    M = int(N)
    X = M / 10 ** res
    V = round(X, 2)
    # 9999 같은 경우 정수 부분이 2자리 이상으로 변함. 이 경우 처리.
    if V > 9:
        V = V / 10
        res += 1    # N의 갯수도 + 해줘야함.
    key = round(V, 1)
    print(f'#{tc} {key}*10^{res}')