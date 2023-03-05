from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home',home,name="home"),
    path('blog',index,name='index'),
    path('index',index,name='index2'),
    path('login',Login,name="login"),
    path('signup',signup,name="signup"),
    path('signout',signout, name="signout"),
    path('newblog',newblog,name='newblog')
]
