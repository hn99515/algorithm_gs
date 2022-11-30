N = int(input())
arr = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))

# 딕셔너리 설정 후 배열 내 같은 숫자 나오면 더해주기
cnt = {}
for num in arr:
    # 값이 들어있다면 +1
    if num in cnt:
        cnt[num] += 1
    else:
        # 없으면 1부터 시작
        cnt[num] = 1

# 찾아야 하는 값을 순회
for card in cards:
    # cnt 딕셔너리에 해당 값이 없으면
    ans = cnt.get(card)
    # 0을 출력!
    if ans == None:
        print(0, end=' ')
    else:
        print(ans, end=' ')