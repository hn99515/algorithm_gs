# M = 자기 점수 중에 최댓값을 고른다.
# 그리고 나서 모든 점수를 점수/M * 100 으로 고친다.
# 새로운 점수로 새로운 평균을 구하자.

N = int(input()) # 시험 본 과목의 수

scores = list(map(int, input().split())) # 기존 점수를 리스트로 담기
M = max(scores) # 최대값 선정

new_scores = [] # 새로운 점수를 담는 리스트
for score in scores: # 기존 점수 1개씩 확인하기 위해 순회
    new_M = score / M * 100 # 새로운 점수로 변경
    new_scores.append(new_M) # 새로운 점수 담기

print(sum(new_scores) / len(new_scores)) # 평균