import sys

sys.stdin = open('s_input.txt')

# 단조 증가함수 찾기. 문자열로 변경해서 한글자씩 비교 단조 증가수 예 111566 단조증가수 아닌예 999888
def increase(num):
    number_str = str(num)
    for k in range(len(number_str)-1):
        # 이전 숫자가 다음숫자보다 크면 단조증가 수가 아니다. 
        if number_str[k] > number_str[k+1]:
            return False
    return True




T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 정곤이 숫자 리스트
    num_list = list(map(int, input().split()))

    max_num = 0
    # 정곤이가 선택할 수있는 2가지 숫자의 곱. 탐색
    for i in range(N-1):
        for j in range(i+1, N):
            num = num_list[i]*num_list[j]
            #단조 증가 수 최대 갱신
            if increase(num):
                max_num = max(max_num,num)

    if max_num ==0:
        max_num =-1

    print(f'#{tc} {max_num}')



