t = int(input()) #  테스트 케이스
for s in range(t): #  만큼 반복
    i, j = input().split() #  R S 입력 받음.
    for u in j: #  S 1개씩 i만큼 곱해줌
        print(u * int(i), end='') #  end=''안하면 값 밑으로 출력됨
    print() #  이거 안 해주면 위에 값 옆에 입력해야함.