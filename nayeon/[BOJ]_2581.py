M = int(input())
N = int(input())

def min_v(lst):
    min_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val



sum_x = 0
result = []
for x in range(M,N+1):
    possible = 0

    for i in range(1,x+1):
        if x % i == 0:
            possible += 1
    if possible == 2:
        sum_x += x
        result.append(x)

if len(result) == 0:
    print(-1)
else:

    print(sum_x)
    print(min_v(result))