# 체스판 다시 칠하기

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
arr_min = []


#N과 M이 8보다 클 때, 큰 숫자 만큼 1씩 더해줌
for i in range (N-7): 
  for j in range (M-7):
    num1 = 0
    num2 = 0

    for a in range(i, i+8):
      for b in range(j, j+8):
        if (a+b) % 2 == 0: 
          if arr[a][b] != 'W':   # W가 아닐때 
            num1 += 1            # W로 칠해주는 갯수
          else:				     # B가 아닐때
            num2 += 1            # B로 칠해주는 갯수

        else:
          if arr[a][b] != 'B':
            num1 += 1
          else:
            num2 += 1 

    arr_min.append(num1)     # 체스판이 W로 시작할때 경우의 수
    arr_min.append(num2)     # 체스판이 B로 시작할때 경우의 수

print(min(arr_min))

# 다시 풀어볼 문제!