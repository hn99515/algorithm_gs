'''
N개의 자연수는 모두 다른 수이다.
N개의 자연수 중에서 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
'''
def dfs(s):      # start
    if len(stack) == M:
        print(*stack)
        return
    else:
        for i in range(s, N):
            # 배열 내 원소를 고르는 것
            if arr[i] not in stack:
                stack.append(arr[i])
                dfs(i+1)
                stack.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

stack = []

dfs(0)

