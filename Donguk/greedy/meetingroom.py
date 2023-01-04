n = int(input())
meeting = []

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

# 끝나는 시간을 기준으로 정렬
meeting.sort(key=lambda x : (x[1], x[0]))

end_time = 0
cnt = 0
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1

print(cnt)