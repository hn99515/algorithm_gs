# 콜드바흐의 추측



# 반드시 다시 풀어봐야 하고 스터디 때 다른 분들의 풀이를 듣고 싶다.

# --------
# 시간초과 발생 코드

# T = int(input())

# for tc in range(T):
#     n = int(input())  # 짝수 n
#     sosu = 0

#     for num in range(n, 3, -1):
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:  # 약수가 존재하는 경우
#                 break         # 더 이상 검사할 필요 x
#         else:
#             sosu = num
#             if n - sosu == 1:
#                 continue
    
#     sosu_1 = n - sosu
#     if sosu > sosu_1:
#         print(sosu_1, sosu)
#     else:
#         print(sosu, sosu_1)