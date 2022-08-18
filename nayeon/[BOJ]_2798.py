# 첫번째 방법
import itertools

N, M =  map(int,input().split())
nums = list(map(int, input().split()))
comb = itertools.combinations(nums,3)

sum_lst = []
for x in comb:
    sum_lst.append(sum(x))

ans = []
for sums in sum_lst:
    if sums <= M:
        ans.append(sums)
print(max(ans))


# 두번째 방법
total = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if nums[i] + nums[j] + nums[k] > M:
                continue
            else:
                total = max(total, nums[i] + nums[j] + nums[k])