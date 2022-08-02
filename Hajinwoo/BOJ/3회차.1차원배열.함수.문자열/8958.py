n = int(input())
for i in range(n):
    m = list(input())
    sum = 0
    j = 1
    for i in m:
        if i=='O':
            sum += j
            j += 1
        else:
            j = 1
    print(sum)