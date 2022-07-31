arr_st = set() # 중복을 제거하려면 set 구조 사용

for i in range(10): # 10개의 수를 받기 위해 순회
    a = int(input())
    n = a % 42 # 42로 나눈 나머지 파악
    arr_st.add(n) # set에 하나씩 넣기

print(len(arr_st)) # 총 개수는 길이로 구하자!