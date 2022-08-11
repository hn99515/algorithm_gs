N = int(input())

#  N킬로그램을 배달해야 한다.
#  설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
cnt = 0
while 1:
    if N % 5 == 0 :
        cnt += (N // 5)
        break
    N -= 3
    cnt += 1
