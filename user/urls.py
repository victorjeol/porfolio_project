from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.login, name="logout"),
    path('register', views.register, name="register"),

]


