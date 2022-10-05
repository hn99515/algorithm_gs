N = int(input())

one = 1         # N 과 비교할 첫 번째 값
dif = 6         # 계차가 6
count = 1       # 최소 방문 횟수

while N > one:  # 주어진 값이 비교값보다 크면 무한 루프
    count += 1  # 방문 횟수에 +1
    one += dif  # 비교값 +계차
    dif += 6    # 계차가 등차수열이므로 +6
print(count)

