# 십자카드 문제

# 숫자 입력
nums = list(map(int, input().split()))

# 시계수 찾기
def get_clock_num(n):
    min = int(''.join(map(str, n)))
    for i in range(1,4):
        tmp = int(''.join(map(str, n[i:]+n[:i])))
        if min > tmp:
            min = tmp
    return min

clk_num = get_clock_num(nums)
cnt = 1
# 1111부터 clk_num까지의 시계수 갯수 count
for i in range(1111, clk_num):
    if '0' not in list(str(i)) and i == get_clock_num(list(map(int, str(i)))):
        cnt += 1
print(cnt)