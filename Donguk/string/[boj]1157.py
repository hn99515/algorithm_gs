# 대소문자를 대문자로 통일
# 가장 많이 사용된 알파벳을 대문자로 출력
# 가장 많은 알파벳 수가 같으면 ?로 출력 (값 비교 필요!)

words = input().upper()                     # 대문자로 통일
word_list = list(set(words))                # 중복 제거
cnt = []                                    # 개수 리스트

for word in word_list:
    cnt.append(words.count(word))            # 각 문자별 개수를 리스트에 담기

if cnt.count(max(cnt)) >= 2:                # 최대값이 중복인 경우
    print('?') 
else:                                       
    print(word_list[cnt.index(max(cnt))]) # 최대값을 인덱스로 출력