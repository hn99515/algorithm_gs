# 자신이 원하는 햄버거와 음료를 하나씩 골라, 세트로 구매하면,
# 가격의 합계에서 50원을 뺀 가격이 세트 메뉴의 가격
# 햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류

sang = int(input())
joong = int(input())
ha = int(input())

coke = int(input())
cider = int(input())

buger = [sang, joong, ha]
bev = [coke, cider]

price = []
for i in buger:
    for j in bev:
        price.append(i+j-50)

print(min(price))
