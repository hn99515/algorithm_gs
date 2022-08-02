numss = [x for x in range(1,10001)]


def aaa(nums):
    result = set()  # 중복 제거를 위해 set 생성
    
    for m in nums:  # 1~10000 사이 수일때
        
        if m + sum(list(map(int, list(str(m))))) in nums:   # ex) 33 + sum([3,3]) 값이 10000까지의 수에 속할때
            result.add(m + sum(list(map(int, list(str(m))))))   # 셋에 추가
    return result

for i in aaa(numss)^set(numss):     # 셀프넘버가 아닌 셋과 10000까지의 수가 담긴 셋의 겹치지않는 부분 출력

    print(i)

