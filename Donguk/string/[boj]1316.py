N = int(input())
res = N                                 # 입력값(개수)을 넣고 시작(조건에 맞지 않는 것은 제외시킨다.)

for i in range(N):                      # 개수만큼 순회
    words = input()
    
    for j in range(len(words)-1):       # 단어의 인덱스만큼 순회
        if words[j] == words[j+1]:      # 그 다음 문자와 같으면 pass
            pass
        elif words[j] in words[j+1:]:   # 끝까지 확인하여 같은게 있다면 -1 (그룹단어 제외)
            res -= 1
            break                       # 반복문 종료
print(res)        
