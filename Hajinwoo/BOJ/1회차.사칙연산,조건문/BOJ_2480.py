a, b, c = map(int, input().split())

if 6 >= a >=1:
    if 6 >= b >=1:
        if 6 >= c >=1:
            if a == b == c :
                print(10000+a*1000)
            elif a==b and a != c:
                print(1000+a*100)
            elif b==c and c != a:
                print(1000+b*100)
            elif a==c and b != a:
                print(1000+a*100)
            elif a != b != c :
                if a > b and a > c:
                    print(a*100)
                elif b > a and b > c:
                    print(b*100)
                elif c > b and c > a:
                    print(c*100)
                else:
                    pass
            else:
                pass
        