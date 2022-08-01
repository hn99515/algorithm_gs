# OX퀴즈

N = int(input())

for i in range(N):
    ans_list = list(input())
    score = 0
    sum_score = 0  # 점수 합계
    for j in ans_list:
        if j == 'O':
            score += 1  # O가 연속되면 1씩 커진다.
            sum_score += score
        else:
            score = 0  # X가 나오면 score 값 리셋
    print(sum_score)

# score과 sum_score을 나누지 않아서 결과가 나오지 않았다.
# 구글링으로 해결..ㅠㅠ