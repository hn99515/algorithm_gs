'''
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys

N = int(input())
stack = []

for _ in range(N):
    order = list(sys.stdin.readline().split())

    if len(order) == 2:
        stack.append(order[-1])
    else:
        if order[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print('-1')
        elif order[0] == 'size':
            print(len(stack))
        elif order[0] == 'empty':
            if stack:
                print('0')
            else:
                print('1')
        elif order[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print('-1')