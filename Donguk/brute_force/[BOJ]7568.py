'''
키와 몸무게, 이 두 개의 값으로 등수를 매겨보려고 한다. 
어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다.
두 사람 A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다.

만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 
이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다. 
아래는 5명으로 이루어진 집단에서 각 사람의 덩치와 그 등수가 표시된 표이다.
'''
N = int(input())
arr = []
for tc in range(N):
    x, y = map(int, input().split())
    # tuple 형태로 한 쌍 묶어서 리스트에 저장
    arr.append((x, y))

# brute-force    
for i in arr:
    # 순위 초기화
    rank = 1
    for j in arr:
        # 튜플 인덱싱 = x는 x끼리 y는 y끼리 비교 / 조건 만족하면 +1
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank)
       