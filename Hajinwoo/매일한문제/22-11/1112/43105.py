import sys
sys.stdin = open('input.txt')

def solution(triangle):
    # 젤 앞에 1개 제외 그 후로 계산
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] +=



triangle = input()
solution(triangle)