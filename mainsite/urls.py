from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
  path('', views.home , name = 'esports-home' ),
  path('user/profiles/',views.Profile,name='user-profile'),
  path('user/notifications/',views.notifications,name='user-notification'),
  path('user/rankings/',views.rankings ,name = 'user-rankings'),
  path('user/practiceScrims/',views.practiceScrims , name='user-scrims'),
  path('logout/',views.logout,name = 'user-logout')
]
