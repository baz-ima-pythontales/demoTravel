from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('index', views.index, name='index'),


]
