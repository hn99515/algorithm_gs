# 프로그래머스 pizza 문제

import sys
sys.stdin = open('input_pizza.txt')

def solution(n):
    answer = 1
    while True:
        if (answer * 6) % n == 0:
            return answer
        else:
            answer += 1
