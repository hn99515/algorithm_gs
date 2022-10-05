'''
플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 고른다.
플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만든다.

M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력
'''
N, M = map(int, input().split())
card_numbers = list(map(int, input().split()))

res = 0
# 3장의 모든 카드 조합을 확인
for i in range(len(card_numbers)):
    for j in range(i+1, len(card_numbers)):
        for k in range(j+1, len(card_numbers)):
            # 카드 3장의 합이 M 이하인 경우
            if card_numbers[i] + card_numbers[j] + card_numbers[k] <= M:
                # 최대값 구하기
                if card_numbers[i] + card_numbers[j] + card_numbers[k] > res:
                    res = card_numbers[i] + card_numbers[j] + card_numbers[k]

print(res)

