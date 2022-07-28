t = int(input())
number = 1
for i in range(t):
    a, b =list(map(int, input().split()))
    print(f'Case#{number}: {a} + {b} = {a + b}')
    number += 1