import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(str, input()))
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    res = 0
    for i in range(min(len(abc)+1, len(arr))):
        if arr[i] == abc[i]:
            res += 1
        else:
            break
    print(f'#{tc} {res}')