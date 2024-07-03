from django.contrib import admin
from django.urls import path
from wst import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home")
]