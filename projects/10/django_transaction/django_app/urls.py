from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path('', views.create_users, name=''),
    path('check/', views.check, name='check'),

    path('api/public/get_all_books/', views.get_public_all_books, name='get_public_all_books'),
    path('api/private/get_all_books/', views.get_private_all_books, name='get_private_all_books'),

    path('api/post_create_user/', views.post_create_user, name='post_create_user'),
]
