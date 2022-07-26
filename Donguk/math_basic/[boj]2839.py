'''
설탕을 정확하게 N킬로그램을 배달해야 한다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램
'''

N = int(input())

if N % 5 == 0:                  # 5로 나누어서 딱 떨어지는 경우
    print(N // 5)
else:                           # 5로 안떨어지는 경우
    cnt = 0
    while N > 0:
        N -= 3                  # 3kg 빼서 봉지 1개 사용
        cnt += 1                
        if N % 5 == 0:          # 다시 5kg에 나눠지는 경우 = 3 + 5 조합
            cnt += N // 5
            print(cnt)
            break
        elif N == 1 or N == 2:  # 3kg, 5kg 봉지로 못 담는 경우
            print(-1)
            break
        elif N == 0:            # 3kg으로만 담는 경우
            print(cnt)
            break

