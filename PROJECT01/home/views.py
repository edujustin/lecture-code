from django.shortcuts import render, HttpResponse
from datetime import datetime
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
# 자기소개
def hola(request):
    return render(request, 'hola.html')
    
# 야식메뉴 
def midnight(request):
    menus = ['라면', '떡볶이', '김밥', '순대국']
    dinner = random.choice(menus)
    return render(request, 'midnight.html', {'menus':menus, 'dinner':dinner})
    
# 로또번호 추출기 - 6개 숫자 --> range(1, 46)  
# random.sample(iterable, 몇개 뽑을 지)

def lotto(request):
    numbers = range(1, 46)
    lottos = random.sample(numbers, 6)
    real_lottos = [6, 10, 16, 28, 34, 38]
    return render(request, 'lotto.html', {'lottos':lottos, 'real_lottos':real_lottos})
    
def dinner(request):
    menus = ['pizza', 'bob', 'chicken', 'sushi']
    picked = random.choice(menus)
    return render(request, 'dinner.html', {'menus':menus, 'picked':picked})
    
def hello(request, name):
    return render(request, 'hello.html', {'name':name})
    
def cube(request, num):
    nums = num ** 3 
    return render(request, 'cube.html', {'num':num, 'nums':nums})
    
# 이름/나이를 받아 template에서 (name)의 나이는 (age)입니다. 라고 출력
def introduce(request, name, age):
    return render(request, 'introduce.html', {'name':name, 'age':age})

def times(request, num1, num2):
    num3 = num1 * num2
    return render(request, 'times.html', {'num1':num1, 'num2':num2, 'num3':num3})
    
def area(request, r):
    a = (r ** 2) * 3.14
    return render(request, 'area.html', {'r':r, 'a':a})
    
# isbirth

def isbirth(request):
    today = datetime.now() 
    if today.month == 5 and today.day == 8:
        result = True
    else:
        result = False
    return render(request, 'isbirth.html', {'result':result})
    
def template_example(request):
    my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
    messages = ['apple', 'banana', 'cucumber', 'mango', 'watermelton', 'kiwi']
    empty_list = []
    
    return render(request, 'template_example.html', {'my_list':my_list, 'messages':messages, 'list':empty_list})

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data':data})

def catch(request):
    return render(request, 'catch.html')

# artii API를 통해 ascii 아트로 변환하여 보여주는 페이지
def result(request):
    #1. form 태그로 날린 데이터를 받는다. (GET 방식)
    word = request.GET.get('word')
    
    #2. ARTII api로 보낸 응답 결과를 text로 fonts라는 변수에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    #3. fonts(str)를 fonts(list)로 바꿔준다.
    fonts = fonts.split('\n')
    
    #4. fonts(list)안에 들어있는 요소중 하나를 선택해서 font라는 변수에 저장한다.
    font = random.choice(fonts)
    
    #5. 위에서 우리가 만든 word와 font를 가지고 다시 arttii로 요청을 보낸 후에 해당 응답 
    #  결과를 result 라는 변수에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    
    return render(request, 'result.html', {'result':result})
    
def throw(request):
    return render(request, 'throw.html')

def get(request):
    name = request.GET.get('name')
    lottos = range(1, 46)
    picked = random.sample(lottos, 6)
    return render(request, 'get.html', {'name':name, 'picked':picked})
    
def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    return render(request, 'user_create.html', {'name':name, 'pwd':pwd})
    
def static_example(request):
    return render(request, 'static_example.html')