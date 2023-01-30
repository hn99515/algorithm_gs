'''
기타를 시리얼 번호 순서대로 정렬하고자 한다.
모든 시리얼 번호는 알파벳 대문자 (A-Z)와 숫자 (0-9)로 이루어져 있다.

시리얼번호 A가 시리얼번호 B의 앞에 오는 경우는 다음과 같다.
1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
'''

N = int(input())

res = []
for _ in range(N):
    s = input()

    tmp = 0     # 자리 수의 합
    for i in s:
        if i.isdigit():
            tmp += int(i)
    res.append((s, tmp))

res.sort(key=lambda x:(len(x[0]), x[1], x[0]))

for i in res:
    print(i[0])