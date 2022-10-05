nums = []
for i in range(9):

    nums.append(int(input()))
max_num = max(nums)
max_idx = nums.index(max_num)

print(f'{max_num}\n{max_idx+1}')

