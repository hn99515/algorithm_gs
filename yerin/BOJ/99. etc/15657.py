# N과 M (8)

def dfs(start):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(start, N):  # 중복 숫자도 허용
        temp.append(lst[i])
        dfs(i)
        temp.pop()

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
temp = []

dfs(0)