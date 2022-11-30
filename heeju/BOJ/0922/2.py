n = int(input())

arr = list(map(int, input().split()))

res = []

for i in range(1,len(arr)):
    if i%2 ==1:
        res.append(arr[i])


for j in range(len(arr)):
    if j%2 ==0:
        res.append(arr[j])


print(res)
