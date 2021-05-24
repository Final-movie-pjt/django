# chat/urls.py
from django.urls import path 
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:room_pk>/', views.enter_room, name='room'),
]
