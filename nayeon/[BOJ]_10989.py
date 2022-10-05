import sys
input = sys.stdin.readline  # 코드 제일 위에 추가한다면, input이 sys.stdin.readline의 속도를 갖는다.

lst = [0]*10001

N = int(input())

for _ in range(N):
    lst[int(input())] += 1
for i in range(len(lst)):
    if lst[i] >= 1:
        for j in range(lst[i]):
            print(i)