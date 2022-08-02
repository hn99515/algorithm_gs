T = int(input())


for i in range(T):
    case = list(map(int,input().split()))       # 각 케이스
    N = case[0]     # 각 케이스의 첫번째 값은 학생의 수
    scores = case[1:]   # 학생들의 점수 리스트 재설정
    avg_score = sum(scores) / N     # 평균 점수
    cnt = 0
    for score in scores:
        if score > avg_score:
            cnt += 1        # 평균 점수 보다 큰 학생수 세기
    percent = cnt / N * 100 # percent로 변환해서 셋째자리까지
    print(f'{percent:.3f}%')
