import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N 배열, M 파리채
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0
    # 파리채 크기를 제외한 배열 크기 (index error 방지)
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리채 크기만큼 움직이기
            total = 0
            for x in range(M):
                for y in range(M):
                    res = arr[i+x][j+y]
                    total += res
            # 최대값 찾기
            if total > maxV:
                maxV = total
    print(f'#{tc} {maxV}')


