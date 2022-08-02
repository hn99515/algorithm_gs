# 단어 수 = 공백 개수 +1

sentence = input()
cnt = 1
for word in sentence:
    if word == ' ':
        cnt += 1

print(cnt)