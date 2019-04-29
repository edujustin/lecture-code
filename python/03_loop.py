
# n = 0 
# while n < 5:
#     print('대표님. 열심히 일하겠습니다.')
#     n = n + 1

# foods = ['pizza', 'pasta', '떠뽀끼', '순대']

# for food in foods:
#     print(food)


numbers = [1, 2, 3, 4, 5, 6]

#1. numbers에서 for문을 사용해 요소를 꺼내, 각각의 요소에 2를 곱해주세요.
# for number in numbers:
#     print(number*2, end=' ,')
# 추가미션: 2를 곱한 값을 new_numbers 라는 새로운 리스트에 담아주세요


for number in numbers:
    new_numbers = [] # 여기서 값이 계속 초기화된다.
    new_numbers.append(number*2)

print(new_numbers)

# 추가미션2: 구구단 만들기 - 2중 for