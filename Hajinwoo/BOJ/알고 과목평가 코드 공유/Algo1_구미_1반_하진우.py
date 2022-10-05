# import sys
# sys.stdin = open('input.txt')

def summary(arr):
    x = 0
    for i in range(len(arr)):
        x += arr[i]
    return int(x)
def maxland(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr[-1]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    rc = list(map(int, input().split()))
    ai = [list(map(int, input().split())) for _ in range(n)]
    land = []
    for i in range(rc[0], rc[2]+1):
        for j in range(rc[1], rc[3]+1):
            land.append(ai[i][j])
    # 범위 값만 담기위한 리스트 land를 만들어 줌.
    qna = summary(land) // len(land)
    # sum함수를 구현해서 평균값 qna를 구해줌.
    cnt = 0
    num = maxland(land)
    for m in range(int(num)):   # 단순히 len(land)만큼만 돌리면 부족!
        for k in range(len(land)):
            if land[k] > qna:
                land[k] -= 1
                cnt += 1
            elif land[k] < qna:
                land[k] += 1
                cnt += 1
    print(f'#{tc} {cnt}')
