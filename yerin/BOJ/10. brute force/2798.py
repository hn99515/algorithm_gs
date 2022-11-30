# 블랙잭

# N: 카드의 총 개수
# M을 넘지 않으면서 최대한 가까운 카드 3장의 합 구하기

n, m = map(int, input().split())  
card_list = list(map(int, input().split()))
card_len = len(card_list)

sum = 0
for i in range(0, card_len - 2):
        for j in range(i + 1, card_len - 1):
                for k in range(j + 1, card_len):
                        if card_list[i] + card_list[j] + card_list[k] > m:
                                continue
                        else:
                                sum = max(sum, card_list[i] + card_list[j] + card_list[k])


print(sum)

# 다시 풀어볼 문제..!