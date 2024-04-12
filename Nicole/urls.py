from django.urls import path
from . import views

urlpatterns = [
    path('Nicole', views.Nicole, name='Nicole'),
    path('base', views.base, name='base'),
    path('login', views.login, name='login'),
    path('courses', views.courses, name='courses'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),


]