while True:
    sen = input()
    if sen == '.':
        break

    stack = []
    temp = True
    for i in sen:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if len(stack) == 0 or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()

        elif i == ']':
            if len(stack) == 0 or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if temp == True and len(stack) == 0:
        print('yes')
    else:
        print('no')