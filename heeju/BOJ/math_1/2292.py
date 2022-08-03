'''
# 벌집
1부터 시작
6의 배수로 커진다
N : N번방까지 지나간다

'''


N = int(input())

honey_num= 1

cnt = 1 # 1부터 반복문 더하고 시작하기때문에 1로 시작/ 반복문 횟수 

while N > honey_num: # 만약에 N 이 반복 시작점 보다 크다면 
    honey_num += 6 *cnt
    cnt+=1

print(cnt)
