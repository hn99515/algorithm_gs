n = int(input())



nums = list(map(int,input().split()))

maxlst = []
minlst = []
for i in range(n):
    if len(maxlst)==0:
        maxlst.append(nums[i])
    else:
        if maxlst[-1] < nums[i]:
            maxlst.append(nums[i])

max__ = maxlst[-1]

for i in range(n):
    if len(minlst)==0:
        minlst.append(nums[i])
    else:
        if minlst[-1] > nums[i]:
            minlst.append(nums[i])

min__ = minlst[-1]

print(min__,max__)