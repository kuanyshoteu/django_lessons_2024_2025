from django.contrib import admin
from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', profile, name = 'profile'),
    path('setimage/', isBogdan, name = 'profile'),
]
