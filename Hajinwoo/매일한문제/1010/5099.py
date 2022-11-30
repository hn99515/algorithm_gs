import sys
sys.stdin = open('input.txt')
from collections import deque

'''
피자는 1번위치에서 넣거나 뺄 수 있다.
    - pop left
화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
    - 선형 큐, 조건 만족 못하면 dont pop -> to last idx
M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 
이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
    - 1번 자리에 왔을 때 C//2 한 후 조건 확인
치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.
    - 말 그대로 ㅇ
'''

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = deque(list(map(int, input().split())))
    idx = deque([i for i in range(1, M + 1)])
    while 1:
        if len(arr) == 1:
            break
        if arr[0] != 0:
            arr[0] = arr[0] // 2
            if arr[0] == 0:
                arr.popleft()
                idx.popleft()
            else:
                arr.append(arr.popleft())
                idx.append(idx.popleft())
    print(f'#{tc} {idx[0]}')