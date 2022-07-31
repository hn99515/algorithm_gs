T = int(input())            # 테스트 개수 입력
res = ''                    # 결과값을 담을 변수 생성

for i in range(T):          # 테스트 수만큼 순회
    R, S = input().split()  # 반복횟수와 문자열 입력

    for j in S:             # 문자열 순회
        res += j * int(R)   # 문자열 하나에 반복횟수 곱하기
    
    print(res)
    res = ''                # 출력 후 초기화