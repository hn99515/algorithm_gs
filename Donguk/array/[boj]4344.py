# 학생들의 평균을 구하고
# 평균을 넘는 학생 수를 구한다
# 평균을 넘는 비율을 구한 뒤 소수점 3째자리까지 반올림해서 표현

C = int(input())                             # 테스트 개수

for i in range(C):                           # 개수만큼 순회
    scores = list(map(int, input().split())) # 인원과 점수를 입력한 뒤 리스트로 받기

    n = scores[0]                            # 총 인원 = 0번째 자리
    score = sum(scores[1:])                  # 총점수 = 1번째 자리 ~ 끝까지
    avg = score / n                          # 평균

    cnt = 0                                  # 평균을 넘는 인원 수를 세는 변수
    for j in scores[1:]:                     # 점수만 순회
        if j > avg:                          # 점수가 평균보다 높은 경우 +1
            cnt += 1

    res = cnt / n * 100
    print(f'{res:.3f}%')                     # 결과값이 소수점 3째자리까지 다 나와야 한다!