n = int(input())

num_list = list(map(int, input().split()))

max_num = max(num_list)

new_num = []

for i in num_list:
     new_num.append(i / max_num *100)


avg = sum(new_num)/len(new_num)

print(avg)

