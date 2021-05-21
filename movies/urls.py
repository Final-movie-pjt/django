from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('init/', views.init, name='init'),
    path('genres/<int:genre_id>', views.get_movies, name='get_movies'),
    path('detail/<int:pk>/', views.detail, name='detail'),
]
