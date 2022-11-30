'''
반복 수열
 - D[1] = A
 - D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합
 예를 들어 A=57, P=2일 때, 수열 D는 [57, 74(=52+72=25+49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …]
반복되는 부분을 제외했을 때, 수열에 남게 되는 수들의 개수
'''
# 각 자리 수 제곱 후 합을 구하는 함수
def square_sum(A, P):
    a = str(A)
    ans = 0
    for i in a:
        ans += int(i) ** P
    return ans


def dfs(A, P, i):
    # 방문자 표시가 0이 아닌 경우 = 반복이 시작됨을 의미
    if visited[A] != 0:
        # 반복이 시작된 n번째에서 -1 하면 반복을 제외한 총 개수
        return visited[A] - 1
    else:
        visited[A] = i
        B = square_sum(A, P)
        i += 1
        return dfs(B, P, i)


A, P = map(int, input().split())
# 방문 횟수 체크를 위해 리스트 최대치로 생성
visited = [0] * ((9**5) + (9**5) + (9**5) + (9**5) + (9**5))
# 1번부터 시작
i = 1

print(dfs(A, P, i))
