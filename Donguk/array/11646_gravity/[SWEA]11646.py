'''
낙차가 가장 큰 상자를 구하여 그 낙차를 리턴 하는 프로그램
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = 0            # 낙하 최대값 찾기
    for i in range(N):
        cnt = 0         # 낙하 횟수 세기
        for j in range(i+1, N):
            # 끝까지 다 돌렸을 때 뒤에 것보다 크기만 하면 무조건 낙차 +1
            if arr[i] > arr[j]:
                cnt += 1
        # 최대값 찾기
        if cnt > maxV:
            maxV = cnt

    print(f'#{tc} {maxV}')