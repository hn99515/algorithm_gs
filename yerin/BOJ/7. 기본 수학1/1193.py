x = int(input())  # 몇 번째 분수?

line = 0
end = 0  # 끝점
# 짝수 line : 시작점 ~ 끝점으로 갈수록 분자 +1, 분모 -1
# 홀수 line : 시작점 ~ 끝점으로 갈수록 분자 -1, 분모 +1

while x > end:  # 몇 번째 line에 있는가? 그 line의 끝점은?
    line += 1
    end += line

diff = end - x            # x와 끝점 차
if line % 2 == 0:         # 짝수 line일 때
    top = line - diff     # 분자
    bottom = diff + 1     # 분모
else:                     # 홀수 line일 때
    top = diff + 1        # 분자
    bottom = line - diff  # 분모

print(f'{top}/{bottom}')

# 약간의 도움을 받은.. 문제... ㅠㅠ

