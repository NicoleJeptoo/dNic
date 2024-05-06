from django.urls import path
from . import views

urlpatterns = [
    path('Nicole', views.Nicole, name='Nicole'),
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    path('login', views.login, name='login'),
    path('courses', views.courses, name='courses'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create/', views.create_course, name='create_course'),

    path('addstudent', views.addstudent, name='adding student'),


    path('editstudent/<id>', views.editstudent, name='editing'),
    path('deletestudent/<id>', views.deletestudent),



]