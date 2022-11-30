import sys
sys.stdin = open('input.txt')

def dfs(num):
    key[num] = False
    for i in adj[num]:
        if key[i] == True:
            dfs(i)


T = int(input())
for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    arr = [list(map(int, input().split()))for _ in range(E)]
    S, G = list(map(int, input().split()))
    adj = [[]for _ in range(V+1)]
    key = [True]*(V+1)
    for i in range(E):
        adj[arr[i][0]].append(arr[i][1])
    dfs(S)

    if key[G] == True:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')