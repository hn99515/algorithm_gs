'''
반복순열
'''


from sys import stdin

A, P = map(int, stdin.readline().split())
check = [A]

while True:
    new = 0
    # 새로운 수 계산
    for i in (str(check[-1])):
        new += int(i) ** P
    # 새로운 수가 check라는 리스트 안에 있으면
    if new in check:
        while True:
            if new == check.pop():
                print(len(check))
                exit()
    else:
        check.append(new)