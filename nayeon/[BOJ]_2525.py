h, m = map(int, input().split())
plus = int(input())

if m + plus >= 60:   
    h_plus = (m + plus)//60
    m = plus % 60 - (60 - m)
    
    if h + h_plus >= 24:
        h = h + h_plus - 24
        print(h,m)
    else:
        h += h_plus
        print(h,m) 
        

else:
    m += plus
    print(h,m)

