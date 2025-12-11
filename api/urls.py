# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.create_user_view, name='create_user'),
    path('users/<int:user_id>/', views.get_user_view, name='get_user'),
    path('users/<int:user_id>/update/', views.update_user_view, name='update_user'),
    path('users/<int:user_id>/delete/', views.delete_user_view, name='delete_user'),
]