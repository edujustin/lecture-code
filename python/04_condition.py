'''
a = 5 
if a > 5:
	print('5 초과')
else:
	print('5 이하')


# num = int(input('숫자를 입력해주세요: '))

# if num % 2 == 1:
#     print('홀수입니다.')
# elif num / 3 == 1:
#     print('아몰라')
# else:
#     print('짝수입니다.')
    
    
#1. 네이버 미세먼지-> 조건문 코드로 작성 (4개 조건)
dust = int(input('오늘의 미세먼지 농도를 입력하세요: '))

if dust > 150:
    print('매우 나쁨')
elif 80 < dust <= 150:
    print('나쁨')
elif 30 < dust <= 80:
    print('보통')
else:
    print('좋아요')


    
#2. 추가미션: 1부터 10 사이의 정수 중 -> 짝수는 짝수 리스트에 홀수는 홀수 리스트 출력 (range(1, 11)

even_numbers = []
odd_numbers = []

for i in range(1, 11):
    if i % 2:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)

print(f'짝수 리스트는 {even_numbers}, 홀수 리스트는 {odd_numbers}')


#1. 집합처럼 중복을 허용하지 않는 리스트 만들기 

numbers = [2, 4, 6, 7, 4, 3, 1, 2, 3]
new_numbers = []

for number in numbers:
    if number not in new_numbers:
        new_numbers.append(number)
print(sorted(new_numbers))

#2. fizzbuzz
# 조건 - 1부터 100까지의 숫자중!
#1. 만약 해당 숫자가 3으로 나누어지면 'Fizz'
#2. 만약 해당 숫자가 5로 나누어지면 'Buzz'
#3. 만약 해당 숫자가 3고 5로 모두 나누어지면 'FizzBuzz'

for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

예시 출력)
         1 월
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7 
 8  9 10 11 12 13 14 
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 
         2 월
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7 
 8  9 10 11 12 13 14 
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 

         3 월
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7 
 8  9 10 11 12 13 14 
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 

         4 월
Mo Tu We Th Fr Sa Su 
 1  2  3  4  5  6  7 
 8  9 10 11 12 13 14 
15 16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30
'''