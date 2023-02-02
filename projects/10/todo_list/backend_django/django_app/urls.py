from django.urls import path, include, re_path
from django_app import views


urlpatterns = [
    path('', views.home, name="home"),
    path('class/', views.GetAllTodos.as_view(), name="class"),

    path('api/', views.routes, name="routes"),
    path('api/get_all_users/', views.get_all_users, name="get_all_users"),

    path('api/todos1/', views.todos, name="todos"),  # Read all, Create new
    path('api/todos1/<todo_id>', views.todos_id, name="todo_id"),  # Read detail, Delete, Update

    # TODO REST
    re_path(r"^api/todos/$", views.todos_new),               # todo GET all | POST | ...
    re_path(r"^api/todos/(?P<pk>\d+)/$", views.todos_new_id),  # todo GET one | PUT | DELETE | ...
]
