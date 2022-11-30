

students = int(input())

students_list = []

for _ in range(students):
    weight, height = map(int, input().split())
    students_list.append((weight, height))

for i in students_list:
    rank = 1
    for j in students_list:
        # 자신보다 덩치 큰 사람이 몇명인지 세기
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end = ' ')