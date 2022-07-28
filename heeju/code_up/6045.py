num= list(map(int, input().split()))

total = 0
for i in num:
    total += i

avg = round(total/len(num), 2)

print(f'{total} {avg:.2f}')




