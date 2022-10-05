natural_num = set(range(1, 10001))
generate_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generate_num.add(i)

self_num = sorted(natural_num - generate_num)
for i in self_num:
    print(i)