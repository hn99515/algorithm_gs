T = int(input())
groupword = 0

for i in range(T):
    
    W = input()
    err = 0
    for j in range(len(W)-1):   
        if W[j] != W[j+1]:  # aaa/pppa
            new_word = W[j+1:]  # aaa/[pppa]
            if new_word.count(W[j]) > 0 : #[pppa].count(a) > 0
                err +=1 # 그룹단어가 아님 (에러발생!)
    if err ==0: # 에러가 0이면 groupword +1
        groupword +=1

print(groupword)    # 그룹월드의 개수 출력
