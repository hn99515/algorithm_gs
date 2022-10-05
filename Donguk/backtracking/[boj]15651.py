'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다 = 중복 허용
'''
def dfs(L):
    # 인덱스가 M에 도달하면 목표 달성
    if L == M:
        for i in range(M):
            print(res[i], end=' ')
        print()
    else:
        # 수열에 포함될 원소 고르기
        for i in range(1, N+1):
            res[L] = i
            dfs(L+1)


N, M = map(int, input().split())
res = [0] * M
dfs(0)