# 여러줄 받을땐 sys.stdin.readline() (런타임에러방지)
# sys.stdin.readline() 은 개행문자(\n) 포함
# 공백을 기준으로 나눠주면 한줄씩 반환
import sys

n = int(input())

testcase =[]
for i in range(n):
    testcase.append(list(map(int, sys.stdin.readline().split()))) # 2차원 리스트

# [[1,1], [12, 34], [5, 500] ...]


for case in testcase:

    print(sum(case))