from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',signup,name="login"),
    path('home',index,name='index'),
    path('index',index,name='index2'),
    path('login',Login,name="login"),
    path('signup',signup,name="signup"),
    path('signout',signout, name="signout"),
    path('newblog',home2,name='newblog')
]
