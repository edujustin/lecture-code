#1. 클래스 
'''
class Person:
    name = '아이유'
    
    def say_hello(self):
        print(f'Hello!, {self.name}')

class Student:
    pass

iu = Person()
iu.say_hello()
print(iu.name)

Person.say_hello(iu)

iu.name = '홍길동'
print(iu.name)
print(Person.name)

iu.say_hello()
Person.say_hello(iu)

print(isinstance(iu, Person))
print(isinstance(iu, Student))


#2. 클래스 용어 

class Person:  # 클래스 정의
    name = 'justin' # 멤버 변수
    
    def greeting(self): # 멤버 메서드
        print(f'안녕하세요. {self.name}님.')
        
justin = Person() # justin -> Person 클래스의 인스턴스
justin.greeting()
justin.name

#3. self ??

class Person:
    name = '아이유'
    age = '19'
    
    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다. 제 나이는 {self.age}입니다.')

iu = Person()
bob = Person()
iu.greeting()
bob.greeting()
print(iu.name)
print(iu.age)

# 
nam = '?'

class Person:
    name = '홍길동'
    
    def greeting(self):
        print(f'{name}')

p1 = Person()
# print(p1.name)
# print(Person.name)
p1.name = '아이유'
# print(p1.name)
# print(Person.name)
p1.greeting() # 1 -> ?
# Person.greeting(iu) # 2 -> 에러


word = 'Not Class Member'

class Something:
    word = 'Class Member'
    
    def Set(self, msg):
        self.word = msg
    
    def Print(self):
        print(self.word)
        
g = Something()
g.Set('First Message')
g.Print()


#4 

class Person:
    def __init__(self):
        print('응애')
    
    def __del__(self):
        print('빠이')

p1 = Person()


class Myclass:
    
    def __init__(self, value): #4. 
        self.value = value #5.
        print(f'{self.value}가 생성되었습니다.') #6.
        
    def __del__(self):
        print('소멸되었습니다.')
        
def foo(): #2. 
    d = Myclass(10) #3. 
    
foo() #1. 


#5. 클래스 변수 / 인스턴스 변수 

class Person:
    population = 0 
    
    def __init__(self, name):
        self.name = name 
        Person.population += 1

me = Person('justin')
print(me.name)
friend = Person('bob')
print(friend.name)
print(Person.population)
third = Person('john')
print(Person.population)


class MixedNames:
    data = 'spam'
    
    def __init__(self, value):
        self.data = value
        
    def display(self):
        print(self.data, MixedNames.data)
        
x = MixedNames(1)
y = MixedNames(2)
x.display()
y.display()


#6. 상속 

class Person:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다.')
        
class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다. 저의 학번의 {self.student_id}입니다.')
    
    
s1 = Student('Justin', '123456')
s1.greeting()


#8.실습1. 자신에 대한 개인 정보를 클래스로 만들기

class Person:
    name = '김재석'
    age = '19'
    hometown = 'seoul'
    hobby = 'sleeping'
    weight = '72'
    
    def greeting(self):
        print(f'안녕하세요. 저는 {self.name}입니다. 제 나이는 {self.age}이구요, 저의 고향은 {self.hometown}입니다.')
    
justin = Person()
justin.greeting()
'''

#9. 실습2. Teacher / Student (상속X) -> 각각의 클래스에 각기 다른 메소드를 정의하세요.
# __init__

class Teacher:
    
    def __init__(self, student):
        self.student = student 
        
    def shouting(self):
        print(f'야 {self.student}!! 난 선생이고 넌 학생이야!')
    
class Student:
    
    def __init__(self, teacher):
        self.teacher = teacher
        
    def responding(self):
        print(f'{self.teacher}님 죄송합니다. 공부 열심히 할게요')
        
t1 = Teacher('김하늘')
s1 = Student('권상우')
t1.shouting()
s1.responding()