word = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

for a in alpha:
    if a in word:
        print(word.index(a), end=' ')
    else:
        print(-1, end=' ')