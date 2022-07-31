total = [] # 정수를 담을 리스트 생성
for i in range(9): # 9개 순회
    a = int(input()) # 하나씩 출력
    total.append(a) # 리스트에 하나씩 담기

print(max(total)) # 최대값
print(int(total.index(max(total)))+1) # 최대값의 위치 = index + 1