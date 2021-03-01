from django.urls import path     
from . import views

urlpatterns = [
    path('register', views.registration),
    path('login', views.login),
    path('passwordReset', views.passwordReset),
    path('pwResetEmail', views.pwResetEmail),
    path('sendResetEmail', views.emailSent),
    path('addUser', views.addUser),
    path('', views.home),
    path('logout', views.logout)
]