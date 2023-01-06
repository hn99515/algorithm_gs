N = int(input())
first = list(map(int, input().split()))
sec = list(map(int, input().split()))

first.sort() # 0 1 1 1 6

res = []
for i in first:
    max_index = sec.index(max(sec))
    num = max(sec) * i
    res.append(num)
    sec.pop(max_index)
    
print(sum(res))
