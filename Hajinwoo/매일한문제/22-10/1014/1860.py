import sys
sys.stdin = open('1860input.txt')

T = int(input())
for tc in range(1, T+1):
    # N명, M초, K개
    N, M, K = list(map(int, input().split()))
    arr = sorted(list(map(int, input().split())))
    X = max(arr)+1
    key = [0 for _ in range(X)]
    emp = [0 for _ in range(X)]
    for i in range(M,X,M):
        key[i] = K
    print(key)
    for i in range(X):
        emp[i] = sum(key[:i+1]) # sum(key[:i+1])이 현재 빵의 총 개수
        for j in range(N):
            if emp[arr[j]] >= 1:
                for j in range(0,i+1):

