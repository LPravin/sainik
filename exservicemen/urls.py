from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login.url'),
    path('index/', views.index, name='index.url'),
    path('registration/',views.registration, name="registraion.url"),
    path('postregistraion/',views.postregistration, name="postregistration.url"),
]