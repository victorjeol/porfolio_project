from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('service', views.service, name="service"),
    path('contact', views.contact, name="contact"),
    path('project2', views. project2, name="project2"),
    path('po', views.pop, name="po"),
    path('wallpaper', views.wallpaper, name="wallpaper"),
    path('painting', views.painting, name="painting"),
    path('reflector', views.reflector, name="reflector"),

]


