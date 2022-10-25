def solve(a, b):
    res = (a+b)*(a-b)

    return res


a, b = map(int, input().split())
print(solve(a, b))
