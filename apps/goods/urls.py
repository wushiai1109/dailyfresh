from django.contrib import admin
from django.urls import path, include
from goods import views

urlpatterns = [
    path('', views.index, name='index'), # 首页
]
