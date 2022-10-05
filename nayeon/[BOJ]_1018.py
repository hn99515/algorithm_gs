import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

square = [input() for _ in range(N)]

final = []
for i in range(N-8+1):
    for j in range(M-8+1):
        W_case = 0
        B_case = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b) % 2 == 0:
                    if square[a][b] != 'W':
                        W_case += 1
                    elif square[a][b] != 'B':
                        B_case += 1
                elif (a+b) % 2 != 0:
                    if square[a][b] != 'B':
                        W_case += 1
                    elif square[a][b] != 'W':
                        B_case += 1
        final.append(min(W_case,B_case))

print(min(final))



