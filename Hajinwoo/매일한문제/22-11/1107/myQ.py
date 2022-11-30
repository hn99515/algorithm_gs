import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    L, R, Q = list(map(int, input().split()))
    Q_list = list(map(int, input().split()))
    l_list = str(L)
    r_list = str(R)
    key = []
    for i in range(Q):
        A = len(str(Q_list[i]))
        if int(l_list[:A]) <= int(str(Q_list[i])[:A]) <= int(r_list[:A]):
            res = 'O'
            key.append(res)
        else:
            res = 'X'
            key.append(res)
    print(f'#{tc}', ''.join(key))