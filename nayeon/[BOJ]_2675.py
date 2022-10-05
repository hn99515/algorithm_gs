N = int(input())

for i in range(N):
    num, word = input().split()
    num = int(num)
    text = ''
    for char in word:
        text += char*num
    print(text)
