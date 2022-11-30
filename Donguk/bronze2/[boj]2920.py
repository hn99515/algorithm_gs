'''
1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed
'''

jangjo = list(map(int, input().split()))

asc = [1, 2, 3, 4, 5, 6, 7, 8]
desc = sorted(asc, reverse=True)

if asc == jangjo:
    print("ascending")
elif desc == jangjo:
    print("descending")
else:
    print("mixed")

