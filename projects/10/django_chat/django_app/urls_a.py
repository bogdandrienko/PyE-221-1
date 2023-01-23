from django.urls import path
from django_app import views_a

websocket_urlpatterns = [
    path('ws/<slug:room_name>/', views_a.ChatConsumer.as_asgi())
]
