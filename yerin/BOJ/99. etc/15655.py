# N과 M (6)

def dfs(start):
    if len(temp) == M:
        print(*temp)
        return

    for i in range(start, N):
        if lst[i] not in temp:
            temp.append(lst[i])
            dfs(i+1)
            temp.pop()


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))  # 오름차순이어야 하기 때문에 sorted
temp = []

dfs(0)


