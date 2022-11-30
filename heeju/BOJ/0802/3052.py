
num_list = []
for i in range(10):
    n = int(input())
    num_list.append(n)

result = []

for j in num_list:
    s1 = j%42
    result.append(s1)


print(len(set(result)))
