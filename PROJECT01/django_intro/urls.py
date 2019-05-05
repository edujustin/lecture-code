from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('home/lotto/', views.lotto),
    path('home/midnight/', views.midnight),
    path('home/hola/', views.hola),
    path('home/index/', views.index),
    path('admin/', admin.site.urls),
]

