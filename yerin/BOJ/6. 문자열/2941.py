croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia:
    word = word.replace(i, 'a')  # replace 사용하여 동일한 문자열로 대체
print(len(word))