from IPython import embed
'''
#1. 함수를 왜 써야 하는가?

height = 30 
width = 20 

area = height * width
perimeter = 2 * (height + width)
print(f'직사각형의 넓이는 {area}이고, 둘레는 {perimeter}입니다.')

def triangle(height, width):
    area = height * width
    perimeter = 2 * (height + width)
    print(f'직사각형의 넓이는 {area}이고, 둘레는 {perimeter}입니다.')
    
triangle(30, 20)
triangle(50, 20)

#2. 함수의 개념

def greeting():
    print('안녕하세요')

greeting()


#3. 함수의 4가지 종류 

#3-1. 인자/리턴 O
def sum(a, b):
    result = a + b
    embed()
    return result 

c = sum(2, 4)
print(c)

#3-2. 리턴 O

def say():
    print('hi')
    return 'hi'
    
a = say()
print(a)

#3-3. 인자 O

def say(name, age):
    print(f'제 이름은 {name}이고 나이는 {age}입니다.')
    
a = say('justin', 19)
print(a)


#3-4. 인자/리턴 X
def say():
    print('안녕하세요')
    
a = say()
print(a)



# new_numbers = numbers.sort()
# print(new_numbers)
# print(numbers)

numbers = [5, 4, 3, 2, 1]
new_numbers = sorted(numbers)
print(new_numbers)
print(numbers)


def my_min(a, b):
    if a > b:
        return b 
    else:  
        return a
result = my_min(2, 2)
print(result)

def my_func(b, a, c):
    print(f'첫번째는 {a}야. 두번째는 {b}야. 그리고 세번째는 {c}야.')

my_func


def greeting(name='justin'):
    print(f'{name}님 안녕하세요.')
    
greeting()
greeting('좌동철')


def my_sum(a=2, b):
    return a + b 
    
print(my_sum(2))


#1. 인자로 두수를 넘겨서 곱한 값을 return 하는 함수 
# def times(a, b):
#     return a * b
# print(times(2, 4))

#2. 원의 면적을 구하는 함수 만들기(return)
def circle_area(r):
    return 3.14 * (r ** 2)
print(circle_area(4))


#3. 주민번호를 -> 남자 / 여자인지 판단하는 함수
number1 = '530821-1050339'
number2 = '530821-2050339'

def male_felmale(num):
    if num[7] == 1:
        print('남자입니다.')
    else:
        print('여자입니다.')

male_felmale(number1)
male_felmale(number2)


def greeting(age, name='jeju'):
    print(f'{name}은(는) {age}살 입니다.')
    
greeting(19)
greeting(19, 'justin')
greeting(age=19, name='bob')
greeting(name='bob', age=19)
greeting(name='철수', 19)


# print(sep='-', 'hi', 'hi')


def my_func(*args):
    print(args)
    print(type(args))
    return args
    
my_func(1, 2, 3)
my_func(1, 2, 3, 4, 5)
my_func(1, 'a', [1, 2, 3], (1, 2, 3), {'a':1, 'b':2})

def my_dict(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
my_dict(한국어='안녕하세요', 영어='hi', 중국어='니하오')
my_dict(한국어='안녕하세요', 영어='hi', 중국어='니하오', 스페인어='아디오스')


#1. 
my_dict = {'a':1, 'b':2}
#2. 
my_dict = {}
my_dict['한국어'] = '안녕하세요'
my_dict['중국어'] = '니하오'

my_dict = dict(한국어='안녕하세요', 중국어='니하오')


#실습1. 
# 사용자의 입력값(정수)을 받아서, 그 수가 짝수인지 홀수인지 구분하는 함수를 작성하세요
num = int(input('숫자를 입력해주세요: '))

def even_odd(num):
    if num % 2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')

even_odd(num)

#실습2. 리스트 안의 가장 작은 요소를 출력하세요
# items = [1, 2, -8, 0] #1

# def smallest_num_in_list(items): # 2
#     min_num = items[0]
#     for item in items:
#         if item < min_num:
#             min_num = item
#     return min_num

# print(smallest_num_in_list(items)) # 3

# def my_sum(a, b):
#     return a + b
    
# a = my_sum(1, 2)
# print(a)


#실습3. 양의 정수의 합을 구하세요.(*args)
# positive_sum(1, -4, 7, 12) ---> 20 

def positive_sum(*args):
    std_num = 0 
    for number in args:
        if number > 0:
            std_num += number
    return std_num

print(positive_sum(1, -4, 7, 12))
positive_sum(1, 2, 3)
'''

