# 최댓값
num_list = []

for j in range(9):
    n = int(input())
    num_list.append(n)


for i ,  num in enumerate(num_list):
    max_num = max(num_list)
    if num == max_num:
        print(max_num)
        print(i+1)
        break

