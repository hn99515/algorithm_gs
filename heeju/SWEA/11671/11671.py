import sys 

sys.stdin = open('s_input.txt')

# 영향을 미치는 집 탐색후 H> X로 변환 
def check(k,dx,dy,row,col,arr):
    for i in range(1,k+1):
        for j in range(4):
            nx = row + dx[j]*i
            ny = col + dy[j]*i
            if 0<= nx <N and 0<= ny <N and arr[nx][ny] == "H":
                arr[nx][ny] = 'X'
            else:
                continue


# 기지국 A,B,C,를 만났을때 탐색
def find_home(arr):
    # A:1줄 , B:2줄, C:3줄
    map = [('A',1),('B',2),('C',3)]
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]

    for row in range(N):
        for col in range(N):
            # A를 만났을때
            if arr[row][col] == 'A':
                k = map[0][1]
                check(k,dx,dy,row,col,arr)
                
            # B를 만났을때
            elif arr[row][col] =='B':
                k = map[1][1] #2
                check(k,dx,dy,row,col,arr)

            # C를 만났을때     
            elif arr[row][col] =='C':
                k = map[2][1] #3
                check(k,dx,dy,row,col,arr)

    return arr


# 남은 집 카운트
def count_home(arr):
    global cnt
    for a in arr:
        # count 함수를 쓰면 리스트 한줄만 보더라도 바로 체크 가능
        cnt += a.count('H')



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    map_list = [list(input()) for _ in range(N)]
    # 기지국 영향을 미치지 않은 집 개수
    cnt = 0 
    map_list= find_home(map_list)
    count_home(map_list)
    #결과
    print(f'#{tc} {cnt}')

