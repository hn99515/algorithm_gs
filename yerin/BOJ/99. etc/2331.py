# 반복수열

a, p = map(int, input().split())
data = [a]

while True :
  value = 0
  for i in str(data[-1]) :
    value += int(i) ** p

  if value in data :
    break

  data.append(value)

print(data.index(value))