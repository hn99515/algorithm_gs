number = int(input())  # 숫자를 입력 받는다.

for n in range(1, 10):
    ans = number * n  # 곱샘 결과값
    print(f'{number} * {n} = {ans}')