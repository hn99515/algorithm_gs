T = int(input())

for _ in range(T):
    stack = []
    brace = input()
    for i in brace:
        # print(i)
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        else:
            # break 안 걸려도 스택에 괄호가 남았다면 틀린 것
            print('NO')