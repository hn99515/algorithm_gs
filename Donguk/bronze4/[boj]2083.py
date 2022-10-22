name, age, weight = input().split()

while 1:
    if name == '#':
        break

    if int(age) > 17 and int(weight) >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')
