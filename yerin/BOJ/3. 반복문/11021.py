number = int(input())

for n in range(1,number+1):  # 1부터 시작되므로 시작점을 설정해야 한다.
    A, B = map(int, input().split())
    ans = A + B
    print(f'Case #{n}: {ans}')