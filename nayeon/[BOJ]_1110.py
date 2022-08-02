n = int(input())
new = n # 할당 (n은 변하지않음 immutable data) , new는 계속 변하게 될 값
new_list = []
cnt = 0
while True:
    if n in new_list:  # 새롭게 만들어지는 수 리스트에 본래의 n이 있게되면 break
        break

    left = new % 10  # 왼쪽 숫자는 숫자를 10으로 나눈 나머지

    right = new // 10 + new % 10  # 오른쪽 숫자는 각 자릿 수를 더한 값

    if right >= 10:
        right = right % 10  # 각 자릿 수 합이 10이상이면 1의 자리 수만 가져옴

    new = int(str(left) + str(right))  # new 값은 왼쪽 숫자 오른 쪽 숫자 이어붙인 것의 정수 값
    new_list.append(new)  # new값을 리스트에 추가 

    cnt += 1  # 한번 카운트

print(cnt)