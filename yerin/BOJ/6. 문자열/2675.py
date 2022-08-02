T = int(input())  # 테스트 케이스 개수

for i in range(T):
    num, S = input().split()  # 반복 횟수, 문자열
    ans = ''
    for i in S:
        ans += int(num) * i
    print(ans)