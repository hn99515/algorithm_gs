N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)

result = []
for score in scores:
    new_score = score / max_score * 100     # 새롭게 정의한 점수를 result 리스트에 추가
    result.append(new_score)
    
print(sum(result) / N)    # 새로운 평균 값 출력