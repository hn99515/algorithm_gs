# 피자 굽기

import sys
sys.stdin = open('input_5099.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())         # 화덕의 크기, 피자 개수
    pizza = list(map(int, input().split()))  # M개의 피자에 뿌려진 치즈의 양

    cheese = []
    for i in range(M):
        cheese.append([i+1, pizza[i]])  # 리스트에 인덱스와 함께 치즈 값 넣어주기

    in_pizza = cheese[:N]     # 화덕에 N개만 넣을 수 있음
    remain_pizza = cheese[N:]

    while len(in_pizza) > 1:  # 하나만 남을 때까지
        check = in_pizza.pop(0)   # 맨앞 피자 꺼내기
        check[1] //= 2     # 다시 꺼냈을 때 c//2로 치즈양 줄어든다
        if check[1] == 0:  # 꺼냈을 때 0이라면 다음 남은 피자 넣기
            if remain_pizza:
                in_pizza.append(remain_pizza.pop(0))
        else:  # 치즈가 0이 아니라면 다시 넣는다
            in_pizza.append(check)

    print(f'#{tc} {in_pizza[0][0]}')