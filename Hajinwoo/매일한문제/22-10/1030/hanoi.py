def hanoi(st, rd, nd, n, answer):
    if n == 1:
        answer.append([st, rd])
    else:
        hanoi(st, nd, rd, n - 1, answer)
        answer.append([st,rd])
        hanoi(nd, rd, st, n - 1, answer)

def solution(n):
    answer = []
    hanoi(1, 3, 2, n, answer)
    return answer
# *********************************************
# *********************************************
# *********************************************
def f(n):
    answer = []
    def hanoi2(st,rd,nd,n):
        if n==1:
            answer.append([st, rd])
        else:
            hanoi2(st, nd, rd, n-1)
            hanoi2(st, rd, nd, n-1)
            hanoi2(nd, rd, st, n-1)
    hanoi2(1, 3, 2, n)
    return answer