changed = ['c=','c-','dz=','d-','lj','nj','s=','z=']
text = input()




for char in changed:
    if char in text:
      
        text = text.replace(char,'_')   # ljes=njak -> _e__ak
        


print(len(text))    # 6