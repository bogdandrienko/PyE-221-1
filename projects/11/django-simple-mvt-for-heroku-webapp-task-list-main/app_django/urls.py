from django.urls import path, re_path
from . import views

app_name = 'app_name_task_list'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name=''),
    path('home/', views.home, name='home'),
    path('sign_in/', views.sing_in, name='sign_in'),
    path('logout/', views.logout_, name='logout'),
    path('sign_up/', views.sign_up, name='register'),
    path('post/', views.post, name="post"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('post_comment_create/', views.post_comment_create, name='post_comment_create'),

    path('task/create/', views.create, name='create'),
    path('task/<int:task_id>/', views.read, name='read'),
    path('task/list/', views.read_list, name='read_list'),
    path('task/<int:task_id>/update/', views.update, name='update'),
    re_path(r'^task/(?P<task_id>\d+)/delete/$', views.delete, name='delete'),
    path('post_ph/<int:post_id>/', views.post_ph, name='post_ph'),
    # path('post/comment', views.post_comment, name='post_comment')
]
