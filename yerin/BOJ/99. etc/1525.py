# 퍼즐

from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]
BOARD_SIZE = 3
def bfs(start):
    q = deque()
    q.append(start)
    board[start] = 0

    while q:
        now = q.popleft()
        if now == '123456780':
            return board[now]
        loc = now.find('0')
        nowx, nowy = loc % BOARD_SIZE, loc // BOARD_SIZE

        for x, y in zip(dx, dy):
            nx = x + nowx
            ny = y + nowy
            nloc = ny * 3 + nx
            if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE:
                continue
            nowList = list(now)
            nowList[loc], nowList[nloc] = nowList[nloc], nowList[loc]
            nxt = ''.join(nowList)
            if not board.get(nxt):
                board[nxt] = board[now] + 1
                q.append(nxt)
    return -1


board = {}
nowInput = ''
for i in range(BOARD_SIZE):
    nowInput += ''.join(input().split(' '))
print(bfs(nowInput))