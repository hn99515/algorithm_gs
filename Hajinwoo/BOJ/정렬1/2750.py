from os import sep


N = int(input())

def bubble(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

arr = []
for _ in range(N):
    M = int(input())
    arr.append(M)
arr = bubble(arr)
print(*arr, sep='\n')