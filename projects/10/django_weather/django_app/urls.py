from django.contrib import admin
from django.urls import path, include
from django_app import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("users/", cache_page(60 * 5)(views.UserListView.as_view()), name="users"),
    path("usr/", views.usr, name="usr"),
    path("weather/", views.weather, name="weather"),
    path("currency/<str:mul>", views.currency, name="currency"),
]
