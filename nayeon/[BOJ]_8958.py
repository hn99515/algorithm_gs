def score_calcul(quiz):
    num_O = list(quiz.split('X'))

    num_O = list(filter(None, num_O))  # 빈 문자열 제거 (filter함수는 함수란에 None을 넣으면 False를 모두 제거하여 반환)


    score = 0
    for n_O in num_O:
        for i in range(1, len(n_O)+1):
            score += i

    return score

answer = []
T = int(input())
for t in range(T):
    quiz = input()
    answer.append(score_calcul(quiz))
for s in answer:
    print(s)