sen = input()
sen = sen.lower()
vowel = ['a', 'e', 'i', 'o', 'u']

while 1:
    if sen == '#':
        break

    cnt = 0
    for s in sen:
        if s in vowel:
            cnt += 1
    print(cnt)