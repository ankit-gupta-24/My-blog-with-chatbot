from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginForm, name='loginForm'),
    path('loginForm/', views.loginForm, name='loginForm'),
    path('registerForm/',views.registerForm, name='registerForm'),
    path('logoutUser/',views.logoutUser, name='logoutUser'),
    path('profile/<str:username>',views.profile, name='profile'),
    path('changePassword/',views.changePassword, name='changePassword'),
]