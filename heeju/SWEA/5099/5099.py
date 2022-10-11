import sys

sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    N,M = map(int, input().split())
    pizza = list(map(int, input().split()))
    cheeze = []

    for i in range(M):
        cheeze.append([i+1,pizza[i]]) # 리스트에 인덱스와 함께 치즈값 넣어주기

    # print(cheeze)

    in_oven = cheeze[:N]
    # 남은피자
    remain = cheeze[N:]

    while len(in_oven) > 1:
        check = in_oven.pop(0)
        check[1] //= 2  # 오른쪽이 치즈 양 오븐 한바퀴 갈때마다 //2 해주기
        if check[1] == 0: # 치즈가 0이 되면 남은 피자 1개 넣어주기
            if remain:
                in_oven.append(remain.pop(0))
        
        else:
            # 아직 치즈 남았으면 계속 오븐에 넣어주기
            in_oven.append(check)
    # 인덱스 뽑기
    print(f'#{tc} {in_oven[0][0]}')