'''
잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.
'''
import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
q = deque()

for _ in range(k):
    num = int(input())

    if num == 0:
        if len(q):
            q.pop()
        else:
            break
    else:
        q.append(num)

print(sum(q))