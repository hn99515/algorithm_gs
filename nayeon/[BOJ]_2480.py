nums = list(map(int, input().split()))

check_set = set(nums)


if len(check_set) == 1:
    for x in check_set:
        print(10000 + x * 1000)
elif len(check_set) == 2:
    for x in check_set:
        if nums.count(x) == 2:
            print(1000 + x * 100)
else:
    print(max(nums) * 100)


