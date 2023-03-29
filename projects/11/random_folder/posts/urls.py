from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.first),
    # path('', views.second)
    path('', include(views.router.urls)),
]