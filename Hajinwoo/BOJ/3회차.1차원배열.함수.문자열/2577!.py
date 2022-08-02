a = int(input())
b = int(input())
c = int(input())

x = list(str(a*b*c)) # 문자열 슬라이싱
for i in range(10):
    print(x.count(str(i))) # i번째 리스트에 존재하는 문자의 갯수 출력