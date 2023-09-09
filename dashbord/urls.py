from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('dashbord/', views.dashbord, name="dashbord"),
    path('profile/', views.profile, name="profile"),
    path('all_service/', views.all_service, name="all_service"),
    path('pat/', views.painting, name="pat"),
    path('contact/', views.contact, name="cont"),
    path('wallpaper/', views.wallpaper, name="wall"),
    path('reflector/', views.reflector, name="reflect"),
    path('pop/', views.pop, name="pop"),
    path('inde/', views.inde, name="inde"),
    path("<int:pk>/inde", views.inde_delete, name="inde_delete"),
    path("<int:pk>/contact", views.contact_delete, name="contact_delete"),
    path("<int:pk>/pop", views.pop_delete, name="pop_delete"), 
    path("<int:pk>/pro", views.pro_delete , name="pro_delete"),
    path('pro/', views.pro, name="pro"),
    path("<int:pk>/painting", views. pain_delete, name="pain_delete"),
    path("<int:pk>/wallpaper", views. wallpaper_delete, name="wallpaper_delete"),
    path("<int:pk>/reflector", views.reflector_delete, name="reflector_delete"),
    
    

]


