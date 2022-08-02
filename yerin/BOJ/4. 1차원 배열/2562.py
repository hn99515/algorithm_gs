# 최댓값

numbers = []  # 입력받은 9개의 수 저장 리스트
for n in range(9):
    numbers.append(int(input()))

print(max(numbers))  # 최댓값 출력
print(numbers.index(max(numbers)) + 1)  # 최댓값 위치 출력

# max 함수를 쓰지 않고 최댓값을 어떻게 구할까..?    