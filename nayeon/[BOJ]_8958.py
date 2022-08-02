T = int(input())

for i in range(T):
    case = input()  # 케이스 한줄
    result = case.split('X')    # X를 경계로 나눔 ['OO', '' , 'O', '', 'OOO']
    count_O = list(filter(len,result))      # len값이 0이 아닌 경우만 걸러서 count_0 리스트에 담음
    cnt = 0
    for cnt_O in count_O:       # ['OO' ,'O', 'OOO']
        for x in range(1, len(cnt_O) + 1):  # 'OO' : 1+2 / 'O' : 1 / 'OOO' : 1+2+3
            cnt += x        # 0 + 3 + 1 + 6 = 10
    print(cnt)
