N, X = map(int, input().split())
A = list(map(int, input().split())) # N 개의 수를 담는 리스트 생성

for i in A: # 리스트 순회
   if i < X: # 각 원소가 X 보다 작다면
    print(i, end=' ') # 출력하는데 다음 출력값을 공백으로 이어주라.
