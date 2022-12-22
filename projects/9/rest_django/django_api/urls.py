from django.urls import path, re_path
from django_api import views

urlpatterns = [
    path('', views.index, name="index"),

    # TODO rest-api маршруты
    path('todos_native/', views.todos_native),
    path('todos_native/<int:pk>/', views.todos_native),

    re_path(r'^todos_drf/$', views.todos_drf),
    re_path(r'^todos_drf/(?P<pk>\d+)/$', views.todos_drf),
]

# /todos/

# CREATE POST /todos/ 1
# READ GET (one | many) (/todos/id/ | /todos/) 2
# UPDATE PUT | PATCH /todos/id/ 1
# DELETE DELETE /todos/id/ 1
