a, b = list(map(int, input().split()))
c = list(map(int, input().split()))
new_numbers = ''
if len(c) == a:
    for i in range(a):
        if c[i] < b:
            new_numbers += (str(c[i]) + ' ')
        else:
            continue
            
    print(new_numbers)
