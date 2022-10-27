# 진료순서 정하기

def solution(emergency):
    emergency_1 = sorted(emergency, reverse=True)
    answer = []
    for i in range(len(emergency)):
        answer.append(emergency_1.index(emergency[i]) + 1)
    return answer