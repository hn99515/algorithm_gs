number = int(input())

for n in range(1, number+1):
    A, B = map(int, input().split())
    ans = A + B
    print(f'Case #{n}: {A} + {B} = {ans}')