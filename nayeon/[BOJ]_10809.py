alphas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


word_chars = list(input())

for s in alphas:
    if word_chars.count(s) >0:
        print(word_chars.index(s), end=' ')
    else:
        print(-1, end = ' ')