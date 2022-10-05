S = input()                             # 문자를 입력 받기

alphabet = 'abcdefghijklmnopqrstuvwxyz' # 알파벳 26개
total = ''                              # 최종 값들이 들어갈 곳

for i in alphabet:                      # 26개 알파벳 순회
    if i in S:                          # 알파벳 중 입력 받은 문자에 있는 경우
        total += str(S.find(i))         # find 함수로 인덱스 값을 넣고
        total += ' '                    # 공백 넣기
    else:                               # 없으면
        total += str(S.find(i))         # find 함수 = -1 값을 넣기
        total += ' '

print(total)