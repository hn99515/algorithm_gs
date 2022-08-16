N = int(input())

num = 2
while N != 1:
    if N % num != 0:
        num += 1
    else:
        print(num)
        N = N // num
