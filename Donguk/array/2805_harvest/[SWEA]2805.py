import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # pointer 생성
    s = e = N // 2

    res = 0
    for i in range(N):
        # s~e 까지 열 탐색
        for j in range(s, e+1):
            res += arr[i][j]
            
        if i < (N//2):      # i 가 절반보다 작은 경우 포인터 늘리기
            s -= 1
            e += 1
        else:               # 반대의 경우 포인터 줄이기
            s += 1
            e -= 1
    
    print(f'#{tc} {res}')