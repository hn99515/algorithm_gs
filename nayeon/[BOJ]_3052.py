rest = set()
for i in range(10):
    num = int(input())
    rest.add(num % 42)  # 10개의 입력값을 각각 42로 나눈 나머지를 rest셋에 추가

print(len(rest))    # 셋의 최종 길이 출력 (셋은 중복 값 불가)