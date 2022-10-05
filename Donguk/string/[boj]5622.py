alpha = input()         # 알파벳 대문자 입력

count = 0               # 최소시간 체크
for i in alpha:         # 알파벳 순회
    if i in 'ABC':      # 해당 문자열에 맞는 경우 각 시간만큼 +
        count += 3
    elif i in 'DEF':
        count += 4
    elif i in 'GHI':
        count += 5
    elif i in 'JKL':
        count += 6
    elif i in 'MNO':
        count += 7
    elif i in 'PQRS':
        count += 8
    elif i in 'TUV':
        count += 9
    elif i in 'WXYZ':
        count += 10

print(count)