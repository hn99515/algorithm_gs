'''
피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.
덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램

피자는 1번위치에서 넣거나 뺄 수 있다.
화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다.
이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.
'''
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # 화덕의 크기, 피자 개수
    N, M = map(int, input().split())
    arr = list(enumerate(map(int, input().split()), 1))   # 치즈의 순번과 양

    fire = arr[:N]      # 화덕에 들어가는 피자
    q = arr[N:]         # 남아있는 피자
    # 마지막 하나가 남으면 종료
    while len(fire) != 1:
        for i in range(N):
            # 한 개 남아있으면 종료
            if len(fire) == 1:
                break

            num, chz = fire.pop(0)
            chz = chz // 2      # 치즈의 양은 절반으로 준다.
            # 치즈가 남아있는 경우 - 다시 화덕에 넣어주기
            if chz != 0:
                fire.append((num, chz))
            elif chz == 0 and len(q) != 0:      # 치즈 양이 0이고 q가 아직 있으면 넣기
                fire.append(q.pop(0))

    res = fire.pop()[0]     # 남아있는 피자의 번호만 출력
    print(f'#{tc} {res}')