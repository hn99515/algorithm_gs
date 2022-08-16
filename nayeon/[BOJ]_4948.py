def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**(0.5)+1)):
            if n % i == 0:
                return False
        return True

range_list = list(range(2,246912))
temp = []

for n in range_list:
    if is_prime(n):
        temp.append(n)

n = int(input())
while True:
    cnt = 0
    if n == 0:
        break


    for i in temp:
        if n < i <= 2*n:
            cnt += 1

    print(cnt)
    n = int(input())
    