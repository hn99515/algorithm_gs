#체커

N = int(input())
result = N
for i in range(0,N):
    word=input()
    for j in range(0,len(word)-1):
        if word[j]==word[j+1]:
            pass
        # 만약에 인덱스 j+1 뒤에서 존재한다면 그룹단어아니다
        elif word[j] in word[j+1:]:
            result-=1
            break
print(result)