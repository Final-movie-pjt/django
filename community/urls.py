from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('<int:pk>/', views.community_detail, name='community_detail'),
]
