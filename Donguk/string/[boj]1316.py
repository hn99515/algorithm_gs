N = int(input())

for i in range(N):
    words = input()

    count = 0
    for l in range(len(words)):
        if words[l] != words[l+1]:
            if words[l] not in words[l+2:]:
                count += 1
        else:
            if words[l] != words[l+2:]:
                if words[l] not in words[l+2:]:
                    count += 1
            else:
                

            
        
