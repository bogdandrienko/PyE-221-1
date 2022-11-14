from django.contrib import admin
from django.urls import path
# from .views import index
from django_app import views
from .views import post

urlpatterns = [
    path('', views.index, name=''),

    path('posts/<int:post_id>/', post),  # TODO одиночный пост
    path('posts/', views.posts),  # TODO массив постов

    path('todo/<int:todo_id>/', views.todo),  # TODO одиночный пост
    path('todo/', views.todo),  # TODO массив постов
]
