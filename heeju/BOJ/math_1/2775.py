'''
부녀회장이 될테야 


3층 1   5   15  35  70
2층 1   4   10  20  35
1층 1   3   6   10  15
0층 1   2   3   4  5

k층 n호 몇명?

t는 테스트케이스
'''
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    # 0층
    floor_0 = [i for i in range(1, n +1)]

    for j in range(k):
        for s in range(1, n):
            # 이전값 더해주기 
            floor_0[s] += floor_0[s-1]
    print(floor_0[-1])




