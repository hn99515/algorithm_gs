l = int(input())    # 방학 총 일수
a = int(input())    # 국어 숙제 페이지
b = int(input())    # 수학 숙제 페이지
c = int(input())    # 하루에 국어 최대 페이지
d = int(input())    # 하루에 수학 최대 페이지

lang = a // c
mat = b // d

ans = 0
if lang >= mat:
    if a % c:
        ans = l - lang - 1
    else:
        ans = l - lang
elif lang < mat:
    if b % d:
        ans = l - mat - 1
    else:
        ans = l - mat

print(ans)