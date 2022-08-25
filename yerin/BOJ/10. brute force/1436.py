# 영화감독 숌

N = int(input())
six = 666
cnt = 0

while True:
    # 현재 제목이 666을 포함되어있다면 cnt 카운트
    if '666' in str(six):
        cnt += 1

    # cnt가 구해야하는 n번째 영화라면 six 출력
    if cnt == N:
        print(six)
        break

    # 제목 카운트
    six += 1