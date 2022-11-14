from django.urls import path
from django_twitter_app import views

app_name = 'django_twitter_app'  # django_twitter_app:home
urlpatterns = [
    path('', views.home_view, name=''),
    path('index/', views.HomeView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.login_f, name='login'),
    path('logout/', views.logout_f, name='logout'),

    # path('post/ratings/', views.posts),
    path('post/create/', views.post_create, name='post_create'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/detail/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # path('post/<int:pk>/comment/detail/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/create/', views.post_comment_create, name='post_comment_create'),
    # path('post/<int:pk>/comment/update/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/comment/delete/', views.post_comment_delete, name='post_comment_delete'),
]
