# 방 번호 : YXX or YYXX

t = int(input())  # 테스트 케이스 수

for _ in range(t):
    h, w, n = map(int, input().split())  # 층 수 / 각 층의 방 수/ 몇 번째 손님
    
    # n이 h의 배수일 때, 아닐 때 나눔
    if n % h == 0:        
        head = h          # head : Y or YY      
        tail = n // h     # tail : XX
    else:
        head = n % h
        tail = (n // h) + 1

    print(f'{head*100 + tail}')
    
# 오랜만에 완전히 내 힘으로 푼 문제 ㅠㅠㅠ 이 맛에 알고리즘 풀지..
# 정답율이 낮길래 쫄았지만 조금만 더 고민하면 쉽게 풀 수 있는 문제였다.
# '기본수학' 단계 문제는 종이에 적어 가면서 풀면 쉽게 풀 수 있다. 