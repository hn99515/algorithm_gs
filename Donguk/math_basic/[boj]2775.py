T = int(input())

for _ in range(T):
    f = int(input())                    # 층
    n = int(input())                    # 호
    arr = [x for x in range(1, n+1)]    # 0층의 사람 수를 리스트로 저장

    for k in range(f):                  # 각 층을 순회
        for i in range(1, n):           # 각 호실을 중복 순회
            arr[i] += arr[i-1]          # 사람 수 업데이트
    print(arr[-1])
    
