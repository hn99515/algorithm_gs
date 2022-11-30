N = int(input())

def bbb(N):
    cnt = 0
    
    for i in range(1,N+1):
        lst = list(map(int, list(str(i))))
        if len(lst) <= 2:       # 한자리수, 두자리수는 어차피 한수 
            cnt +=1
        elif len(lst) ==3:          # 세자리수일때는 ex. 123 -> 2-1 = 3-2 확인 필요
            if lst[2] - lst[1] == lst[1] - lst[0]:
                cnt +=1
        else:       # 이외의 경우는 1000밖에없는데 한수 아니라서 pass!
            pass
    return cnt


      
print(bbb(N))