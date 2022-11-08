while True:
    numbers = list(map(int, input().split()))

    if sum(numbers) == 0:
        break

    numbers_sq = []
    for i in numbers:
        numbers_sq.append(i ** 2)

    numbers_sq.sort()
    if numbers_sq[0] + numbers_sq[1] == numbers_sq[-1]:
        print('right')
    else:
        print('wrong')
