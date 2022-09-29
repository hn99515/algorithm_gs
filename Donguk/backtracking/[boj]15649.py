'''
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''
def dfs():
    if len(stack) == M:         # stack의 길이가 M개이면 조건 만족
        print(*stack)
        return

    for i in range(1, N+1):
        # 방문한 적 없다면 방문 표시
        if i not in stack:
            stack.append(i)       # 결과값 저장
            dfs()                 # 함수 재실행
            stack.pop()


N, M = map(int, input().split())
stack = []

dfs()
