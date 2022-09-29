import sys
sys.stdin = open('input.txt')

"""
1. 고른 수열은 오름차순이어야 한다.
    = 뒷 숫자는 앞 숫자보다 크다.
2. 중복되는 수열을 여러 번 출력하면 안되며
    = not in [] 형식
"""
def dfs(start):
    if len(key) == M:
        print(*key)
        return
    for i in range(start, N+1):
        if i not in key:    # 중복을 걸러준다.
            key.append(i)   # 중복이 아니면 숫자 i를 리스트에 추가.
            dfs(i+1)        # M보다 커지는 경우는 모두 X
            key.pop()

if __name__ == '__main__':
    N, M = map(int, input().split())
    key = []
    dfs(1)                  # 공집합 제외 1부터 시작