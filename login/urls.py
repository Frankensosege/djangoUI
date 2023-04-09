from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/(?<name>)', views.home, name='welcome'),
    path('register/', views.register, name='register'),
]