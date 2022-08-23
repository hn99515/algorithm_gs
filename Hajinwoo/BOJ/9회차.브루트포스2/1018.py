N, M = map(int, input().split())        # 10 13
arr = [input() for _ in range(N)]
stack = []
for i in range(N-7):                    # 인덱싱
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for x in range(i, i + 8):       # 인덱싱
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:    # 좌표 값의 합이 짝수일 때
                    if arr[x][y] == 'B':
                        cnt1 += 1       # B의 개수
                    if arr[x][y] == 'W':
                        cnt2 += 1       # W의 개수
                else:                   # 좌표 값의 합이 홀수일 때
                    if arr[x][y] == 'W':
                        cnt1 += 1       # W의 개수
                    if arr[x][y] == 'B':
                        cnt2 += 1       # B의 개수
        stack.append(min(cnt1, cnt2))   # 짝홀이 BW 인 경우 cnt 1  | 짝홀이 WB 인 경우 cnt 2 둘 중 작은 값을 stack
print(min(stack))                       # stack 안에서도 가장 작은 값이 최소의 경우 값