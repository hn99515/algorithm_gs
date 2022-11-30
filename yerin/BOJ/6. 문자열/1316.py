N = int(input())

group_word = 0
for i in range(N):
    word = input()
    no = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성: 0부터 단어개수 -1까지
        if word[index] != word[index+1]:  # 연달은 두 문자가 다를 때
            new_word = word[index+1:]  # 현재 글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재 글자가 있었다면
                no += 1  # no에 1씩 증가
    if no == 0:
        group_word += 1  # no가 0이면 그룹단어

print(group_word)

# 이거 구글링해서 풀었다 ㅠㅠㅠ 못 풀었다 ㅠㅠㅠ