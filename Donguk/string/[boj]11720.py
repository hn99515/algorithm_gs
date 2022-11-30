N = int(input())    # 숫자 개수 입력
n = input()         # 개수만큼 숫자 입력

total = 0           # 합을 계산할 변수
for i in n:         # 문자열 순회
    total += int(i) # 숫자로 변환 후 모두 합

print(total)
