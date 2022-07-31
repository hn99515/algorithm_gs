N = int(input())
new = N # 미리 할당해놓고 시작
new_list = [] # 더해서 나오는 새로운 수를 담기
count = 0

while True:
    if N in new_list: # 같은 숫자가 나오면 끝!
        break

    one = new % 10 # 나머지 = 일의 자리수
    two = new // 10 # 몫은 = 십의 자리수
    three = new // 10 + new % 10 # 더해서 나오는 새로운 수
    
    if three > 9: # 새로운 수가 10이상이면
        three = three % 10 # 1의 자리수만 택한다

    new = int(str(one) + str(three)) # 새로운 수
    new_list.append(new) # 새로운 수 담기

    count += 1 # 한 바퀴 돌면 +1

print(count)  

