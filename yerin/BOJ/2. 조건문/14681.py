point_x = int(input())
point_y = int(input())

if point_x > 0 and point_y > 0:
    print(1)
elif point_x < 0 and point_y > 0:
    print(2)
elif point_x < 0 and point_y < 0:
    print(3)
else:
    print(4)