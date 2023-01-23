from django.urls import path
from django_app import views

urlpatterns = [
    path("data/", views.data, name="data"),
    path("", views.rooms, name="rooms"),
    path("<slug:slug>/", views.room, name="room")
]
