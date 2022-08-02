mult = 1
for i in range(3):
    num = int(input())
    mult *= num     # 3개의 input을 곱한 정수가 mult

mult_lst = list(str(mult))      # 정수 mult를 str으로 형변환 후 list로 변환 ['1','7','0','3','7','3','0','0']
ints = [x for x in range(0,10)]     # 0~9 까지 수


for i in ints:  # 0~9까지의 수가 각각 mult_lst에서 몇번씩 나왔는지 count하여 출력
    print(mult_lst.count(str(i)))