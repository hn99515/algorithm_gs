# 달팽이가 올라가는 높이 A, 내려가는 높이 B, 나무 길이 V
# 올라갔다가 내려온 높이가 나무 길이보다 작으면 무한 루프

A, B, V = map(int, input().split())
# h = 0           # 달팽이의 높이
# cnt = 0         # 횟수 체크

# while h < V:    # 높이가 나무 길이보다 크면 종료
#     cnt += 1
#     h += A      # 낮에 올라간 높이 더하기
#     if h == V:  # 높이가 5면 반복문 종료
#         break
#     else:
#         h -= B  # 밤에 내려간 높이 빼기
        
# print(cnt)

if A - B > 0:
    cnt = V - A + 1
elif A == V:
    cnt = 1

print(cnt)