# O 가 나오면 +1
# X 가 나오면 다시 0으로 초기화

t = int(input())        # 테스트 개수

for i in range(t):      # 개수만큼 순회
    arr = list(input()) # 리스트에 문자 담기

    s = 0               # 연속된 O를 계산
    total = 0           # 계산된 점수를 합산할 변수
    for j in arr:       # 문자 리스트 순회
        if j == 'O':    # 문자가 O 인 경우 +1 & 합산 변수에 담기
            s += 1      
            total += s
        else:           # 문자가 X 인 경우, s 초기화
            s = 0
    print(total)