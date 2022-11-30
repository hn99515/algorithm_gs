cnt = int(input())  # 정수의 개수
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))

# 최소값, 최대값 출력
# min과 max를 사용하지 않고 풀어보려고 했지만.. 실패ㅠ

#for i in range(numbers):
#    if n <= numbers[n]:
#        n_min = n
#    elif n >= numbers[n]:
#        n_max = n
#print(n_min, n_max)