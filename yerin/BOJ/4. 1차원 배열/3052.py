# 나머지

ans = []
for n in range(10):
    ans.append(int(input()) % 42)

ans = set(ans)  # 셋은 중복되는 원소가 없다! 그 특징 이용
print(len(ans))