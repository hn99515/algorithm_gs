h,m = map(int, input().split())
# 45분 일찍 알람 맞추기 45분 기준, 44보다 크면 
if m > 44:
    print(h, m-45)
# 분이 45보다 작고, 시는 0보다 클때   
elif m < 45 and h >0:
    print(h-1, m+15)
# 분이 45보다 작고, 시는 0보다   
else:
    print(23, m+15)