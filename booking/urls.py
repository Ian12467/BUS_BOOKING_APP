from django.urls import path
from .views import*


urlpatterns = [
    path('', index, name='index'),
    path('users/', users, name='users'),
    path('register/', register, name='register'),
    path('schedule/', schedule, name='schedule')
]
