from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('myblog',myblogs,name='myblogs'),
    path('newblog',newblog,name='newblog'),
    path('dashboard',dashboard,name='dashboard'),
    path("change_password", change_password, name="change_password"),
    path('password-reset', ResetPasswordView.as_view(), name='password_reset'),
]
