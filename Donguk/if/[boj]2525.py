A, B = map(int, input().split())
C = int(input()) # 요리가 진행되는 시간

D = (B + C) // 60 # 시간을 얼마나 + 할 지 확인!
if B + C >= 60: # 분의 합이 60 이상이면
    if A + D >= 24: # 총 시간이 24시를 넘긴 경우
        print(A + D - 24, B + C - (D * 60))
    else: # 총 시간이 24시를 넘기지 않는 경우
        print(A + D, B + C - (D * 60))
else: # 분의 합이 60 미만
    print(A, B+C)