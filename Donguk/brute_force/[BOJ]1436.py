N = int(input())

num = 666
cnt = 0
while True:
    # 문자열은 멤버십 연산 가능
    if '666' in str(num):
        cnt += 1
    # cnt = N 인 경우 = N번째 수를 출력
    if cnt == N:
        print(num)
        break
    # 계속 1을 더해 cnt 와 N이 동일해질 때까지 무한 루프
    num += 1
