import sys
sys.stdin = open('sample_input.txt')


def dfs(v):
    res = []
    # 시작점 방문하고 시작
    visited[v] = 1
    while True:
        for w in adjList[v]:        # v 정점의 인접한 정점 순회
            if visited[w] == 0:     # 방문한 적 없는 인접 정점
                stack.append(w)     # stack 에 넣고
                v = w               # 다음 정점으로 이동
                visited[w] = 1      # 방문 표시
                res.append(v)       # 방문한 정점을 별도 저장
                break
        # 정점이 갈 곳 없을 때
        else:
            if len(stack) != 0:     # 인접 정점을 모두 돌아도 stack이 남아있다면
                v = stack.pop()     # 다음 방문할 곳 pop
            else:
                break
    return res


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    N = V+1

    adjList = [[] for _ in range(N)]
    for _ in range(E):
        a, b = map(int, input().split())
        adjList[a].append(b)

    s, g = map(int, input().split())
    # 방문 정점 리스트, stack
    visited = [0] * N
    stack = []

    res = dfs(s)
    if g in res:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')