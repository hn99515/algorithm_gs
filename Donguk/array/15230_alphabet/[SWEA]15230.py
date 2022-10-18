import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    alphabet = input()
    a = 97

    cnt = 0
    for i in alphabet:
        # a가 나오면 개수 +1
        if ord(i) == a:
            cnt += 1
            a += 1      # 비교할 문자의 ord 값도 +1
        else:           # a가 안나오면 그냥 종료
            break

    print(f'#{tc} {cnt}')
