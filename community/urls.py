from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('create/<int:movie_pk>', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/like/', views.like, name='like'),
]
