import sys
sys.stdin = open('input.txt')
from collections import deque

st = list(map(int, input().split()))
arr = []
while 1:
    if len(arr) == len(st):
        break
    st = deque(st)
    arr.append(st)
    x = st.popleft()
    st.append(x)

key = []
for i in range(len(arr)):
    key.append(list(arr[i]))

emp = []
for i in range(len(key)):
    word = ''
    for j in range(len(arr)):
        word += str(key[i][j])
    emp.append(word)

check = []
for i in range(len(emp)):
    check.append(int(emp[i]))
# 시계수를 구한 집합. check
check.sort()
# 이 중 가장 작은 수
# print(check[0]) # 1122
x = check[0]
many = []
for i in range(1111, check[0]):
    many.append(i)
set(many)
cnt = 0
for i in range(len(many)):
    if '0' in str(many[i]):
        cnt += 1

res = len(many) - cnt

print(res)