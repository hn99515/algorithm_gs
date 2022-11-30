# 참외밭

# import sys
# sys.stdin = open('input_2477.txt')

k = int(input())  # 1m^2의 넓이에 자라는 참외 개수
# [변의 방향, 변의 길이]
# 1: 동쪽, 2: 서쪽, 3: 남쪽, 4; 북쪽
arr = [list(map(int, input().split())) for _ in range(6)]
# print(arr)  -> [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]

width = 0   # 가장 긴 가로변 초기화
w_idx = 0   # 인덱스 초기화
height = 0  # 가장 긴 세로변 초기화
h_idx = 0   # 인덱스 초기화

for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2:  # 동, 서 => 가로
        if width < arr[i][1]:
            width = arr[i][1]
            w_idx = i
    else:  # 남, 북 => 세로
        if height < arr[i][1]:
            height = arr[i][1]
            h_idx = i
# print(width, w_idx, height, h_idx) => 160 1 50 0
#
sub_width = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])
sub_height = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])
# print(sub_width, sub_height)
res = ((width * height) - (sub_width * sub_height)) * k
print(res)