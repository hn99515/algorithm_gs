while True:
    s = input()
    N = len(s)

    if s == 'END':
        break
    else:
        s = list(s)
        for i in range(len(s)//2):
            s[i], s[-1-i] = s[-1-i], s[i]

        for j in s:
            print(j, end='')
        print()