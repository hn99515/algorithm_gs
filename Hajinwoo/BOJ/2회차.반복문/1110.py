n = input()

while True:
    if n:
        break

    x = int(n[0])+int(n[1])
    
    if x >= 10:
        x = int(n[1])+int(x[1])
    else:
        x = int(n[1])+int(x[0])
