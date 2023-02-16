from django.contrib import admin
from django.urls import path, include
from django_app import views

urlpatterns = [
    path('', views.create_users, name=''),
    path('check/', views.check, name='check'),

    path('api/get_all_books/', views.get_all_books, name='get_all_books'),
]
