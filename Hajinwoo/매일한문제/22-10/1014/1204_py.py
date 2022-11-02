import sys
sys.stdin = open('1204input.txt')
'''
최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라
'''
T = int(input())
for _ in range(1, T+1):
    tc = int(input())
    arr = list(map(int, input().split()))
    res = [0 for i in range(101)]
    for i in range(1000):
        res[arr[i]] += 1

    key = max(res)
    result = 0
    for i in range(101):
        if res[i] == key:
            result = i
    print(f'#{tc} {result}')