from django.urls import path, re_path
from . import views

app_name = 'app_name_django_app'  # namespace
urlpatterns = [
    # path('index/', views.index),
    # path('json_api/', views.json_index),
    # path('class/', views.GetUsers.as_view()),

    path('index/', views.index, name='index'),
    path('', views.home, name=''),
    path('home/', views.home, name='home'),

    # path('post/create/', views.create, name='create'),
    # path('post/<int:post_id>/', views.read, name='read'),
    path('post/list/', views.read_list, name='read_list'),
    path('post/<int:post_id>/update/', views.update, name='update'),
    re_path(r'^post/(?P<post_id>\d+)/delete/$', views.delete, name='delete'),  # 'task/<int:post_id>/delete/'
]
