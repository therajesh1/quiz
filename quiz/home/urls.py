from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home',views.index,name='home'),
    path('indexx',views.indexx,name='indexx'),
    path('main',views.main,name='main'),
    path('mainn',views.mainn,name='mainn'),
    path('style',views.style,name='style'),
    path('style2',views.style2,name='style2'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('signup',views.signup,name='signup'),
    path('',views.first,name='first'),
    # path('firsts',views.firsts,name='firsts'),





]