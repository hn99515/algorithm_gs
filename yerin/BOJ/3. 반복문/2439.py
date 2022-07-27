count = int(input())

for star in range(1,count+1):
    print(' ' * (count-star) + '*' * star)
# 오른쪽 정렬을 하기 위해서는 별 앞에 공백이 있어야 한다.