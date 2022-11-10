from django.urls import path
from django_twitter_app import views

app_name = 'django_twitter_app'  # django_twitter_app:home
urlpatterns = [
    path('', views.home_view, name=''),  # TODO HOME
    path('index/', views.HomeView.as_view(), name='index'),  # TODO HOME
    path('home/', views.HomeView.as_view(), name='home'),  # TODO HOME

    # path('post/ratings/', views.posts),
    path('post/', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:pk>/detail/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.post_pk_view, name='post_update'),
    path('post/<int:pk>/delete/', views.post_pk_view, name='post_delete'),
]
