N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")

# 출력이 한 졸로 나오기 위해서 end=" "를 사용해야 한다!