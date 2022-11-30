import sys
sys.stdin = open('input.txt')
'''
1. 계단은 한 번에 한 계단씩 또는 두 계단씩.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막은 반드시 밟아야한다. = 마지막을 밟거나 마지막 바로 전을 밟는다.
참고 : https://sungmin-joo.tistory.com/18
'''

N = int(input())
arr = [int(input()) for _ in range(N)]
dp = []
# 첫번째 칸
dp.append(arr[0])
# 첫번째 칸, 두번째 칸
dp.append(max(arr[0]+arr[1], arr[1]))
# 두번째 칸을 바로 가는 경우, 첫번째를 밟고 가는 경우
dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))
# 세번째칸 까지만 하드코딩, 이후 패턴 찾아서 end와 end-1 중 어느거냐 찾기.
for i in range(3, N):
    dp.append(max(dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i - 1]))

print(dp.pop())