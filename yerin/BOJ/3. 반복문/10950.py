test_case = int(input())  # 테스트 케이스의 수

for i in range(test_case):   # 테스트 케이스만큼 정수 입력받기
    A, B = map(int, input().split())
    print(A + B)

# range(test_case) 대신 test_case만 넣었더니 TypeError가 떴다.
# 정수는 iterable이 아니다!!
# 그렇다고 test_case를 int를 설정하지 않고 입력받으니까 반복이 되지 않는다.

# 새벽에 코딩하니까 재밌고 학구열도 불탄다..ㅎㅎ