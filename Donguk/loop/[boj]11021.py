T = int(input())

total = 0 # 총합 변수 생성
for i in range(1, T+1): # 1~T 까지 순회
    A, B = map(int, input().split())
    total = A + B
    print(f'Case #{i}: {total}')
