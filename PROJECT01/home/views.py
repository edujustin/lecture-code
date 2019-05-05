from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django!')
    
# 자기소개
def hola(request):
    return HttpResponse('My name is Juistin')
    
# 야식메뉴 
def midnight(request):
    menus = ['라면', '떡볶이', '김밥', '라면']
    dinner = random.choice(menus)
    return HttpResponse(f'오늘의 야식메뉴는 {dinner}입니다.')
    
# 로또번호 추출기 - 6개 숫자 --> range(1, 46)  
# random.sample(iterable, 몇개 뽑을 지)

def lotto(request):
    numbers = range(1, 46)
    lottos = random.sample(numbers, 6)
    return HttpResponse(f'오늘의 로또 번호는 {lottos}입니다. 가즈아!!!')