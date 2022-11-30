for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())

    ans_h = h2 - h1
    ans_m = m2 - m1
    ans_s = s2 - s1

    if ans_s < 0:
        ans_s = ans_s % 60
        ans_m -= 1
    if ans_m < 0:
        ans_m = ans_m % 60
        ans_h -= 1

    print(ans_h, ans_m, ans_s)