arr = input().split('-')        # - 기준으로 괄호 치기 위해서 나누기
ans = []
# print(ans)

for i in arr:                   # 배열 순회
    res = 0
    tmp = i.split('+')          # + 기준으로 숫자 나누기
    # print(tmp)
    for j in tmp:               # + 기준으로 나뉜 숫자이기에 더해주기
        res += int(j)
    ans.append(res)             # 더한 결과값은 ans 배열에 담아두기
    
n = ans[0]                      # 배열 내 첫 번째 값
for i in range(1, len(ans)):    # 배열 내 나머지 값을 순회하면서 - 해주면 최소값이 나온다.
    n -= ans[i]
    
print(n)