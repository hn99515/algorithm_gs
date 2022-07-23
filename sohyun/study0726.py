#입출력과 사칙연산
#1
print('Hello World')


#2
print('WE love you krill\nWe love you krill')

#프린트문 2번사용 혹은 \n을 활용


#3
print('\\    /\\')
print(' )  ( \')')
print('(  /  )')    
print(' \(__)|')

#4
print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

# 따옴표 또는 \ 출력을 위해서는 \를 앞에 붙여주면 된다.


#5
numbers = input().split()
print(int(numbers[0]) + int(numbers[1]))

numbers = map(int, input().split())
print(sum(numbers)) 

# w자료를 받기 위해 input을 쓰고 이것을 분해하기 위해 띄어쓰기를 기준으로 split 한다. 이후 인덱스를 활용해 값을 더할 수 있다
# 또는 map 함수로 리스트의 값들을 모두 정수화 한 다음에 sum 함수를 활용할 수도 있다

#6
numbers_2 = input().split()
print(int(numbers[0]) - int(numbers[1]))
#7 #8
# 곱하기는 * 나누기는 / 를 활용한다