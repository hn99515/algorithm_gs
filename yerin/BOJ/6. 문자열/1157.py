words = input().upper()
words_list = list(set(words))  # 입력받은 문자열에서 중복값 제거

count_list = []
for i in words_list:
    count = words.count(i)
    count_list.append(count)  # count 횟수를 리스트에 추가

if count_list.count(max(count_list)) > 1:  # 최대값 수가 여러 개라면!
    print('?')
else:
    max_index = count_list.index(max(count_list))  # 최대값 위치
    print(words_list[max_index])


# 이거 좀 시간 오래걸렸음 ㅠㅠㅠ
