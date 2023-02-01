'''
심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. 
A는 자기보다 크기가 작은 먹이만 먹을 수 있다.
'''

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    pointer = 0
    cnt = 0
    for i in range(N):
        while True:
            # 포인터가 B 배열의 개수만큼 커지는 경우 = A가 B 전체보다 큰 경우
            # A가 B보다 작은 경우 개수 더하고 멈춰야 함
            if pointer == M or A[i] <= B[pointer]:
                cnt += pointer
                break
            else:
                pointer += 1

    print(cnt)