a,b = input().split()

a_ = int(a[::-1])

b_ = int(b[::-1])

if a_ > b_:
    print(a_)
elif a_ < b_:
    print(b_)