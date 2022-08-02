changed = ['c=','c-','dz=','d-','lj','nj','s=','z=']
text = input()



cnt = 0
for char in changed:
    if char in text:
        cnt +1
        text = text.replace(char,'')
print(cnt)