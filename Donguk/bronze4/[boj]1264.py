sen = input()

while True:
    if sen == '#':
        break

    cnt = 0
    for s in sen:
        if s in 'AaEeIiOoUu':
            cnt += 1
    print(cnt)