# 평균

n = int(input())  # 과목의 개수
num_list = list(map(int, input().split()))
M = max(num_list)

num_sum = 0  # 조작된 점수의 합
for i in range(n):
    new_num = num_list[i] / M * 100
    num_sum += new_num
average = num_sum / n   # 평균
print(average)
