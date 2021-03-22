from django.contrib import admin
from django.urls import path, include
from user import views
from user.views import RegisterView, ActiveView, LoginView

urlpatterns = [
    # path('register',views.register,name='register'), # 注册
    # path('register_handle',views.register_handle, name='register_handle'), # 注册处理

    path('register', RegisterView.as_view(), name='register'), # 注册
    path('active/<token>', ActiveView.as_view(), name='active'), # 用户激活
    path('login', LoginView.as_view(), name='login'), # 用户激活
]
