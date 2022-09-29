'''
중복 없이 M 개를 고르는 수열
'''
def dfs(L, s):
    # 상태공간트리의 level = M 은 목표치 도달을 의미
    if L == M:
        for j in range(L):          # 조합의 결과를 출력
            print(res[j], end=' ')
        print()

    else:
        # 시작한 숫자부터 N까지 순회
        for i in range(s, N+1):
            res[L] = i              # 결과 리스트에 삽입
            dfs(L+1, i+1)           # 레벨 +1, 숫자 +1


N, M = map(int, input().split())

res = [0] * (N+1)
dfs(0, 1)   # level, start (출발 숫자)
