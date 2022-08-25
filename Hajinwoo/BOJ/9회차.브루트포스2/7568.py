N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
# [(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]
for i in arr:                           # 1,2,3,4,5
    rank = 1
    for j in arr:                       # 1,2,3,4,5
        if i[0] < j[0] and i[1] < j[1]: # 0 = 몸무게 1 = 키
                rank += 1               # 덩치가 작으면 등수 += 1
    print(rank, end = " ")
