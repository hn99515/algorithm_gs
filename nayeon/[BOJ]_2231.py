import sys
input = sys.stdin.readline
N = int(input())

result = []
for n in range(1,N+1):  # N보다 작은 자연수 중
    digit_sum = sum(map(int,list(str(n))))  #
    total_sum = n + digit_sum
    if total_sum == N:
        result.append(n)
if len(result) == 0:
    print(0)
else:
    print(min(result))