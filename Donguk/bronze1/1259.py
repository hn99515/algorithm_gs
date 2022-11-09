while True:
    numbers = list(map(int, input().split()))

<<<<<<< HEAD
if number = 0:
    break
else:
=======
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
>>>>>>> 0f5752424f5acebd474972a5e3b82289939cf0ea
