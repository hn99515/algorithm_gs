# 소수 구하기

# M이상 N이하의 소수 출력
M, N = map(int, input().split()) 

for num in range(M, N+1):
    if num == 1:  # 1은 소수 x
        continue
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:  # 약수가 존재하는 경우
            break         # 더 이상 검사할 필요 x
    else:
        print(num)

# 특정 수의 제곱근을 구해, 그 제곱근까지의 약수를 구하면 해당 약수를 표함하는 수 제거 가능
# int(sqrt(12)) = 3   -> 12의 약수 3!

# 시간초과가 발생해서 코드를 다시 뜯어고쳤다.
# 구글링을 통해 제곱근을 활용하는 방식을 알게 되었고, 이를 이용하여 코드를 수정했다. 
            

# 시간 초과 발생
# M, N = map(int, input().split()) 

# for num in range(M, N+1):
#     error = 0
#     if num > 1 :
#         for i in range(2, num):  # 2부터 n-1까지
#             if num % i == 0:
#                 error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
#         if error == 0:
#             print(num)