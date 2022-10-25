import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    key = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            key.append(arr[i] * arr[j])
    res = -1
    for i in key:
        emp = []
        k = i
        while k:
            emp.append(k % 10)
            k = k // 10
        for j in range(len(emp) - 1):
            if emp[j] < emp[j+1]:
                break
        else:
            res = i

    print(f'#{tc} {res}')
