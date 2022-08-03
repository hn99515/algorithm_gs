# 손익분기 개념 체크
# A 는 고정비, B는 노트북 대당 총 생산비, C 는 대당 판매가
import math                                 # ceil 메서드 사용을 위해

A, B, C = map(int, input().split())
bep = 0                                     # 손익분기점을 돌파하는 생산 개수

if (C - B) > 0:                             # 생산 대수에 따른 가변 비용 중 C - B > 0 커야만 이익이 발생
    if type(int(A / (C - B))) == int:       # 손익분기를 구하는 식이 정수로 나눠 떨어진다면
        bep += (int(A / (C - B))) + 1       # 생산 대수에 +1 (그래야만 최초로 이익이 나기 때문!)
    else:
        bep += int(math.ceil(A / (C - B)))  # 생산 대수가 정수가 아니라면 올림을 진행
else:                                       # 손익분기가 존재하지 않는 경우
    bep = -1                                

print(bep)