from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('home/static_example/', views.static_example),
    path('home/user_create/', views.user_create),
    path('home/user_new/', views.user_new),
    path('home/get/', views.get),
    path('home/throw/', views.throw),
    path('home/result/', views.result),
    path('home/catch/', views.catch),
    path('home/pong/', views.pong),
    path('home/ping/', views.ping),
    path('home/template_example/', views.template_example),
    path('home/isbirth/', views.isbirth),
    path('home/area/<int:r>/', views.area),
    path('home/times/<int:num1>/<int:num2>/', views.times),
    path('home/introduce/<name>/<int:age>/', views.introduce),
    path('home/cube/<int:num>/', views.cube),
    path('home/hello/<name>/', views.hello),
    path('home/dinner/', views.dinner),
    path('home/lotto/', views.lotto),
    path('home/midnight/', views.midnight),
    path('home/hola/', views.hola),
    path('home/index/', views.index),
    path('admin/', admin.site.urls),
]

