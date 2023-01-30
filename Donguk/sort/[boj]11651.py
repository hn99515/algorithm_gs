'''
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.
baekjoon의 접미사는
baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고,
이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
'''

s = input()

arr = []
# 1개씩 빼서 저장
for _ in s:
    arr.append(s)
    s = s[1:]

arr.sort()
for i in arr:
    print(i)