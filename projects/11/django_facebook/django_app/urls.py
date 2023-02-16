from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('json_api/', views.json_index),
    path('', views.GetUsers.as_view()),
]
