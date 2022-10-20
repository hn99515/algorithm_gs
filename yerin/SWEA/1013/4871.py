# 그래프 경로

import sys
sys.stdin = open('input_4871.txt')

def DFS(now):
    # 1) 방문표시
    visited[now] = 1
    result.append(now)   # 방문 경로 체크
    # 2) 인접 정점 확인
    for nxt in range(V+1):
        if graph[now][nxt] == 1 and visited[nxt] == 0:
    # 3) 이동가능하다면 이동
            DFS(nxt)



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())       # 노드 수, 간선 수

    # 모든 간선정보 받기
    edge_list = [list(map(int, input().split())) for _ in range(E)]
    # 하나의 리스트에 저장
    edge_lists = edge_list[0]
    for i in range(1, E):
        edge_lists.extend(edge_list[i])

    # 경로 존재 확인할 출발, 도착 노드
    check = list(map(int, input().split()))

    # 인접 정점 (행렬로 만들기)
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for idx in range(E):
        frm = edge_lists[idx * 2]
        to = edge_lists[idx * 2 + 1]
        graph[frm][to] = 1

    visited = [False] * (V + 1)
    result = []
    DFS(check[0])

    if check[-1] in result:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')