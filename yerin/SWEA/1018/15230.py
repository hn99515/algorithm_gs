# 알파벳 공부

import sys
sys.stdin = open('input_15230.txt')

T = int(input())
for tc in range(1, T+1):
    alp = list(input())
    ans = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    cnt = 0
    for i in range(len(alp)):
        if alp[i] == ans[i]:
            cnt += 1
        else:
            break

    print(f'#{tc} {cnt}')