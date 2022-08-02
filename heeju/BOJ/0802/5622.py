alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

time = 0
for alpa in alpabet_list :  
    for i in alpa:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 순회
        for n in word :  # 입력받은 문자에서 알파벳 하나씩 순회
            if i == n :  # 알파벳이 같으면
                time += alpabet_list.index(alpa) +3  # time = time + index +3
print(time)