# 구간 합 구하기 4

import sys
# sys.stdin = open('input_11659.txt')

input = sys.stdin.readline
N, M = map(int, input().split())       # 수의 개수, 합을 구해야 하는 횟수
pfs = list(map(int, input().split())) # N개의 수

# 누적 합(prefix sum) 알고리즘 활용
for i in range(N-1):
    pfs[i+1] += pfs[i]
pfs = [0] + pfs

for _ in range(M):
    i, j = map(int, input().split())  # 구간
    print(pfs[j] - pfs[i-1])


# 시간초과 #
# N, M = map(int, input().split())       # 수의 개수, 합을 구해야 하는 횟수
# nums = list(map(int, input().split())) # N개의 수
# for tc in range(M):
#     i, j = map(int, input().split())  # 구간
#
#     ans = sum(nums[i-1:j])
#     print(ans)
