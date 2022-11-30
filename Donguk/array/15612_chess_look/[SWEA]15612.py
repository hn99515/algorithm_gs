'''
각 칸에는 최대 1개의 룩을 놓을 수 있으므로, 체스판 위에는 0개 이상 64개 이하의 룩이 놓여 있는 것
이때, 현재 체스판의 배치가 다음 조건을 모두 만족하는지를 판별하는 프로그램

      - 정확히 8개의 룩이 있어야 한다.
      - 서로 다른 두 룩은 같은 열에 있거나 같은 행에 있으면 안 된다.
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'O':
                cnt += 1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    key = 0
    if cnt == 8:
        for i in range(8):
            for j in range(8):
                for k in range(4):
                    for l in range(1, 8):
                        ni = i + di[k] * l
                        nj = j + dj[k] * l

                        if 0 <= ni < 8 and 0 <= nj < 8 and arr[i][j] == 'O':
                            if arr[ni][nj] == '.':
                                key += 1
                            else:
                                key = 0
                                break

    if key == 14 * 8:
        print(f'#{tc} yes')
    else:
        print(f'#{tc} no')
