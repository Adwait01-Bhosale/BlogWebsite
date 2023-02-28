from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('index',index,name='index2'),

    path('newblog',home2,name='newblog')
]
