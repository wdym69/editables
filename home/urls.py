from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('get_text_file/', views.get_text_file, name='get_text_file'),
    path('save_text_file/', views.save_text_file, name='save_text_file'),
]