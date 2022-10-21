# 수 정렬하기

# 버블정렬 이용
N = int(input())
num_list = []

for _ in range(N):
    num_list.append(int(input()))

for i in range(N):
    for j in range(N):
        if num_list[i] < num_list[j]:
            num_list[i], num_list[j] = num_list[j], num_list[i]

for n in num_list:
    print(n)