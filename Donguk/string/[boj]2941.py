# replace 함수를 통해 문자를 교체
words = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 미리 문자열 리스트 생성
for i in croatia:                                           
    words = words.replace(i, '*')                            # 입력 받은 단어 중 리스트 내에 있는 단어가 있다면 '9'로 변경

print(len(words))