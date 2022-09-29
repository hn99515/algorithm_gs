def dfs():
    if len(stack) == M:         # stack의 길이가 M개이면 조건 만족
        print(*stack)
        return

    for i in range(1, N+1):
        # 방문한 적 없다면 방문 표시
        if visited[i] == 0:
            visited[i] = 1
            stack.append(i)       # 결과값 저장
            dfs()                 # 함수 재실행
            stack.pop()
            visited[i] = 0           # 방문 표시 초기화


N, M = map(int, input().split())

visited = [0] * (N+1)
stack = []

dfs()
