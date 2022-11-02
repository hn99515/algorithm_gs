import sys
sys.stdin = open('input.txt')

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while 1:
    W, H = list(map(int, input().split()))
    if W == 0 and H == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(H)]

    cnt = 0
    for i in range(W):
        for j in range(H):
            if arr[i][j] == 'o':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < W and 0<= ny < H and arr[nx][ny]!='X':
