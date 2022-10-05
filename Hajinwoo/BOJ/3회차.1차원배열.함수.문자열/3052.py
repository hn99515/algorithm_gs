n_list = []
x = []
for i in range(10):
    n_list.append(int(input())) # n_list에 1개씩 담아준다.
    x.append(n_list[i] % 42) 
    # x 리스트에 n_list의 각각의 값을 42로 나눈 나머지를 담는다.
x=set(x) # set으로 list x에 담긴 중복된 값을 제거해준다.
print(len(x)) # len으로 중복된 값이 없는 리스트 x의 길이를 잰다.