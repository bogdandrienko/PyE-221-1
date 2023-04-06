from django.urls import path
from django_app import views


app_name = "django_app"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.Home.as_view(), name=""),
    path("home/", views.Home.as_view(), name="home"),

    path("user/register/", views.register, name="register"),
    path("user/login/", views.login_f, name="login"),
    path("user/logout/", views.logout_f, name="logout"),

    path("post/create/", views.create, name="create"),
    path("post/<int:post_id>/detail/", views.read, name="read"),

    path("post/<int:post_id>/rating/like/", views.rating_like, name="rating_like"),
    path("post/<int:post_id>/rating/dislike/", views.rating_dislike, name="rating_dislike"),

    path("post/<int:post_id>/create_comment/", views.create_comment, name="create_comment"),

    path("post/list/", views.read_list, name="read_list"),
    path("post/<int:post_id>/update/", views.update, name="update"),
    path("post/<int:post_id>/delete/", views.delete, name="delete"),
]
