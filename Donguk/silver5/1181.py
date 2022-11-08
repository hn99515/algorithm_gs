T = int(input())
words = set()
for _ in range(T):
    w = input()
    words.add(w)

words = list(words)

words_sorted = []
for i in words:
    # 단어의 길이와 인덱스를 함께 저장
    words_sorted.append((len(i), i))

# 아래와 같이 정렬하면 길이 순, 사전 순으로 정렬 완료된다.
ans = sorted(words_sorted)

for length, word in ans:
    print(word)