import sys
sys.stdin = open('input.txt')

def mix(arr):
    global res
    for i in range(1, 13):
        if arr[i] != 0:
            if arr[i]*day <= N:
                if arr[i]*day < M:
                    cnt_arr[i] = arr[i]*day
                else:
                    cnt_arr[i] = M
            elif arr[i]*day > N:
                if N < M :
                    cnt_arr[i] = N
                else:
                    cnt_arr[i] = M

T = int(input())
for tc in range(1, T+1):
    day, N, M, year = list(map(int, input().split()))
    arr = [0] + list(map(int, input().split()))
    cnt_arr = [0] * 13

    # print(cnt)       # 몇 달 가는가. // 며칠 가는지도 필요한가?
    # print(arr)       # [0, 0, 0, 2, 9, 1, 5, 0, 0, 0, 0, 0, 0]
    mix(arr)
    emp = []
    for i in range(len(cnt_arr)):
        emp.append(cnt_arr[i])

    for i in range(13):
        if i + 2 <= 12:
            if cnt_arr[i]+cnt_arr[i+1]+cnt_arr[i+2] > M:
                cnt_arr[i] = M; cnt_arr[i+1] = 0; cnt_arr[i+2] = 0
    for i in range(12,-1,-1):
        if i - 2 >= 0:
            if emp[i]+emp[i-1]+emp[i-2] > M:
                emp[i] = M; emp[i-1] = 0; emp[i-2] = 0

    if sum(cnt_arr) > sum(emp):
        cnt_arr = emp

    if sum(cnt_arr) < year:
        res = sum(cnt_arr)
    else:
        res = year
    print(f'#{tc} {res}')