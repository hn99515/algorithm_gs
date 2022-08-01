n=[]
for i in range(9):
    n.append(int(input())) # 리스트에 1개씩 추가해준다.

print(max(n))
print(n.index(max(n))+1) 
# range(9) = 0~8까지. n번째 자릿수를 나타내려면 1부터 세야함.