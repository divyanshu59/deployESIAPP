from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.userAuth,name='user-authentication'),
    path('register/',views.userRegister,name='user-registration'),
    path('register/otp/',views.userRegisterOtp,name='register-otp'),
    path('login/otp/',views.userLoginOtp,name='Login-otp'),
    path('dashboard/',views.userDashboard , name='dashboard'),
] 

