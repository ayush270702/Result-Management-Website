from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),  
    path('login', views.login, name = 'login'),  
    path('stud_login', views.stud_login, name = 'stud_login'),  
    path('teach_login', views.teach_login, name = 'teach_login'),  
    path('signup', views.signup, name = 'signup'),  
    path('logout', views.logout, name = 'logout'),  
    path('stud_profile/<int:pk>/', views.stud_profile, name='stud_profile'),
    path('teacher_profile/<int:pk>/', views.teacher_profile, name='teacher_profile'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), 
    path('update_marks/<str:pk>/', views.test, name='update_marks'), 
    path('div/<slug:div>/', views.div, name='div'), 
    path('tprofile/<int:pk>/', views.profile1, name = 'profile')
]

