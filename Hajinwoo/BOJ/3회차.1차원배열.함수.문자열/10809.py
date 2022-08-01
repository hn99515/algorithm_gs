s = input()
for i in range(97,123): # 아스키코드 소문자 범위
    print(s.find(chr(i)), end=" ") 
    # find로 거기에 있나 없나 찾아봄.
    # 없으면 -1을 반환.