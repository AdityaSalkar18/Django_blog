from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('', views.signuppage,name='signup'),
    path('login', views.loginpage,name='login'),
    path('logout/', views.logoutpage,name='logout'),
    path('myprofile/',views.myprofile, name='myprofile'),
    path('home/',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('createblog/',views.createblog, name='createblog'),
    path('myblog/',views.myblog, name='myblog'),
    path('myfeedbacks/',views.myfeedbacks, name='myfeedbacks'),
    path('editblog/<slug:slug>/',views.editblog, name='editblog'),
    
    path('feedback/<slug:slug>/',views.feedback, name='feedback'),
    path('posts/<slug:slug>/', views.blog, name='blog'),
    
    
    
]

