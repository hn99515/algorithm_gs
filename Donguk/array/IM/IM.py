T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        total = 0
        for k in range(K):
            for h in range(K):
                total += arr[i+k][j+h]
        # 가운데 정사각형 합을 빼야 한다.
        for x in range(1, K-1):
            for y in range(1, K-1):
                total -= arr[i+x][j+y]

        if total > maxV:
            maxV = total

print(f'#{tc} {maxV}')