import sys

test_case = int(input())
for n in range(test_case):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

# 10950. A+B -3 문제와 같은 코드를 사용했더니 시간초과가 떴다.
# 문제에서 input 대신 sys.stdin.readline을 사용하라고 했다.
# 한 번도 사용해 본 적 없는 함수라서 검색을 했고, 공부할 수 있었다.
# 속도가 중요한 경우라면 해당 함수를 사용하는 게 더 이득인 것 같다.
# 하지만 아직은 input()이 더 편하다...