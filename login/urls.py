from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login, name='login'),
    path(r'register/', views.register, name='register'),
    path(r'login/', views.login, name='login'),
]