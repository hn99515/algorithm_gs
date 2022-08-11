# 첫 번째 줄에 Test case의 수 T가 주어진다. 
# 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

T = int(input())
for _ in range(T):
    k = int(input()) # k 층
    n = int(input()) # n 호
    arr = [] # k 층 리스트
    for i in range(1, n+1):
        arr.append(i)