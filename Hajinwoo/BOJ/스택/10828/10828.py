from inspect import stack
import sys

N = int(sys.stdin.readline())

commend = []

for i in range(0,N) :
    commend.append(sys.stdin.readline().split('\n')[0].split(' '))

class Stack:
    stack = []

    def push(cls, X) :
        cls.stack.append(X)
    
    def pop(cls):
        return cls.stack.pop() if cls.stack else -1

    def size(cls):
        return len(cls,stack)
    
    def top(cls):
        return

    def empty(cls):
        return

for j in commend :
    if j[0] == 'top' :
        print(stack.top())
    elif j[0] == 'size' :
        print(stack.size())
    elif j[0] == 'empty' :
        print(stack.empty())
    elif j[0] == 'pop' :
        print(stack.pop())
    else :
        stack.push(j[1])