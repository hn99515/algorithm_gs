H, M = input().split(' ')
H = int(H)
M = int(M)


if 23>= H >=0:
    if 59>= M >= 0:
        if 45 > M:
            if H == 0:
                H+=23
                M += 15
            else:
                H -= 1
                M += 15
        elif M >= 45:
            M -= 45

print(H,M)