'''
 0은 빈 공간, 1은 사냥꾼, 2는토끼, 3은 바위
 ① 사냥꾼은 상하좌우 및 대각선 8방향으로 사격하며, 총알의 개수는 무제한
 ② 사냥꾼끼리는 서로 사격할수 없다.
 ③ 바위 뒤편의 토끼는 사냥할수 없다.

 주어진 배열에서 사냥꾼이 총 몇 마리의토끼를 사냥할 수 있는지 구하라.
'''
import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 사냥꾼 위치 찾기
    hunter = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                hunter.append((i, j))

    # 상하좌우+대각선 = 8방향
    di = [-1, 1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, -1, 1, -1, 1, 1, -1]

    # 사냥꾼 위치에서부터 사냥 시작
    cnt = 0         # 사냥한 토끼 수
    for i in range(len(hunter)):
        r, c = hunter[i]
        for k in range(8):      # 사냥꾼 위치에서 8방향 탐색
            ni = r + di[k]
            nj = c + dj[k]
            # 인덱스 범위 내 + 사냥꾼 X + 바위 X
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and arr[ni][nj] != 3:
                # 토끼를 만나면 사냥
                if arr[ni][nj] == 2:
                    cnt += 1
                # 토끼가 아니면 그 방향으로 쭉 가자
                ni = ni + di[k]
                nj = nj + dj[k]

    print(f'#{tc} {cnt}')
