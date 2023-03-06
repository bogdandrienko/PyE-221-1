from django.urls import path
from .views import read_all_books, temp_create

urlpatterns = [
    path('read_all_books/', read_all_books, name='read_all_books'),
    path('temp_create/', temp_create, name='temp_create'),
]
