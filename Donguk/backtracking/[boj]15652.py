'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

고른 수열은 비내림차순
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순

중복되는 수열을 여러 번 출력하면 안되며,
'''
def dfs(L):
    if L == M:
        for j in range(M):
            print(res[j], end=' ')
        print()
    else:
        for i in range(1, N+1):
            res[L] = i
            dfs(L+1)


N, M = map(int, input().split())
res = [0] * M

dfs(0)