# 덩치

import sys
sys.stdin = open('input_7568.txt')

N = int(input())  # 전체 사람 수

lst = [list(map(int, input().split())) for _ in range(N)]
rank_list = []   # 등수 저장 리스트

for i in range(N):
    rank = 1
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            rank += 1
    rank_list.append(rank)

print(*rank_list)

# swea 풀다가 tc 만드는 게 습관이 됐다.. 그래서 tc 돌리다가 오류나서 다시 보고 수정했다.
