x = int(input())

n = 0                   # x가 몇 번째 대각선인지 체크
max_num = 0             # 대각선 라인 중에 가장 큰 수

while x > max_num:      # x가 가장 큰 수보다 작을 때까지 반복
    n += 1              # x가 크면 대각선 열 +1
    max_num += n        # max_num 은 +line

gap = max_num - x       # 열에서 가장 큰 수 - x
if n % 2 == 0:          # n 이 짝수인 경우
    top = n - gap       # 분자
    bottom = gap + 1    # 분모
else:                   # n이 홀수인 경우
    top = gap + 1
    bottom = n - gap

print(f'{top}/{bottom}')
