from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('create/<int:movie_pk>', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
