x, y, w, h = map(int, input().split())

minV = min(abs(x), abs(y), abs(x-w), abs(y-h))
print(minV)