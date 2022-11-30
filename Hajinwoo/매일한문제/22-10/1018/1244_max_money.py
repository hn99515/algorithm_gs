import sys
sys.stdin = open('max_input.txt')

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    arr = []
    for i in a:
        arr.append(int(i))

    for i in range(b):
        pass