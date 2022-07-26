A, B = map(int,input().split())
C = int(input())
# 60분 기준으로 몫, 나머지 더해주기
A += C // 60
B += C % 60
# 60분 기준으로 시간 +1, 분은 -60 해주기
if B >= 60 :
    A+=1
    B-=60
# 24시간 기준으로 -24 해주기
if A >= 24 :
    A-=24

print('%d %d' % (A,B))