import sys
sys.stdin = open('input.txt')

def solution(arr):
    N = len(arr)
    key = [0]*N
    i = 1
    while True:
        M_num = max(arr)
        if max(arr) == 0:
            break
        key[arr.index(M_num)] = i
        i += 1
        arr[arr.index(M_num)] = 0
        continue

    return key


for tc in range(3):
    arr = list(map(int, input().split()))
    res = solution(arr)

    print(res)