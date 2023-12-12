from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('register/', views.registerUser, name='registerUser'),
    path('register-team/', views.registerTeam, name='registerTeam'),
    path('mentor/', views.mentorDashboard, name='mentorDashboard'),
]
