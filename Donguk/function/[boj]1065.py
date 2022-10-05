# 연속된 두 자리 수가 일정하면 한수
# 한수의 개수를 구하자

N = int(input())                                            # 정수

cnt = 0                                                     # 한수의 개수를 셀 변수 생성
for i in range(1, N+1):                                     # 1~N 까지 순회
    hansoo = list(map(int, str(i)))                         # 순회하는 수를 문자열로 형변환하여 리스트에 담기
    if i < 100:                                             # 100보다 작은 경우 +1
        cnt += 1
    else:                                                   # 100 이상인 경우
        if hansoo[0] - hansoo[1] == hansoo[1] - hansoo[2]:  # 두 개의 연속된 수의 차이가 일정하면 +1
            cnt += 1
print(cnt)