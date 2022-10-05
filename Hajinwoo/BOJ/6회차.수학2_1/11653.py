N = int(input())
m = 2
while N > 1:
    if N % m == 0: # N 이 m으로 나눠질 때
        N = N / m
        print(m)
    else: # N이 m으로 나눠지지 않을 때
        m += 1


# print("================================"*3)
# 처음에 쓰던 방향
# N = int(input())
# while N > 1:
#     if N % 2 == 0: # N이 짝수일 때
#         N = N / 2
#         (?)
#     else: # N이 홀수일 때
#         (?)