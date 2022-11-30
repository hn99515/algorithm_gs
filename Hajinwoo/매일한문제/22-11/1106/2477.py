import sys
sys.stdin = open('input.txt')

K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
arr = arr.sort()

for i in range(6):
    arr[i]