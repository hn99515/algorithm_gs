N = int(input())  # N개의 숫자
nums = input() 

total = 0
for n in range(N):
    total += int(nums[n])  # nums[n]은 문자열이기 때문에 int로 바꿔줘야 함

print(total)