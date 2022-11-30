'''
N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순
'''
def dfs(s):
    if len(stack) == M:
        print(*stack)
        return
    else:
        for i in range(s, N):
            stack.append(arr[i])
            dfs(i)
            stack.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

stack = []

dfs(0)