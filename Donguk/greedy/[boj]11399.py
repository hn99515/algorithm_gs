N = int(input())
arr = list(map(int, input().split()))

arr.sort()

res = 0
wait = 0
for i in arr:
    res += i
    wait += res

print(wait)