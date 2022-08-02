word = list(input().lower())
word_alpha = set(word)  # 대소문자 구분안하니까 전부 소문자로 변환 후, 중복을 제거하여 어떤 문자들이 있는지 파악!

cnts = []
dic = {}
for char in word_alpha:
    cnts.append(word.count(char))   # 해당 단어에서 문자가 몇번 반복되는지 카운트해서 리스트에 담음
    dic[str(word.count(char))] = char   # 가장많이 나온 '문자'를 반환해야하므로, {'1':'a', '3':'b'} 이런형식으로 딕셔너리 생성 
max_cnt = max(cnts)    # 가장 많이 반복된 횟수
if cnts.count(max_cnt) > 1:     # 가장 많이 반복된 횟수 value가 한개가 아닐경우!
    print('?')  # ? 출력
else:    
    print(dic[str(max_cnt)].upper())    # 한개일경우 해당 횟수를 key로하는 문자 value를 대문자로 출력!





