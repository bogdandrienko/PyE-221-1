import time

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.cache import caches
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.views import View

from django_app import models as django_models, utils as django_utils

# Create your views here.

DatabaseCache = caches["default"]
LocMemCache = caches["ram_cache"]


@django_utils.logging_txt_decorator
def index(request):
    return HttpResponse("<h1>This is a Index Page</h1>")


@django_utils.logging_txt_decorator
def index_json(request):
    return JsonResponse(data={"response": "This is a Index Page"}, safe=False)


class Home(View):
    @django_utils.logging_txt_decorator
    def get(self, request, *args, **kwargs):
        context = {"salary": 12352133053, "word": "Привет мир! Привет мир! Привет мир! Привет мир!"}

        return render(request, "django_app/home.html", context)


@django_utils.logging_txt_decorator
def register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', "")
        password2 = request.POST.get('password2', "")

        if password and password != password2:
            raise Exception("пароли не совпадают!")
        if username and password:
            User.objects.create(
                username=username,
                password=make_password(password),
            )

            return redirect(reverse('django_app:login', args=()))
        else:
            raise Exception("данные не заполнены!")
    context = {}

    return render(request, "django_app/user_register.html", context)


@django_utils.logging_txt_decorator
def login_f(request):
    if request.method == "POST":

        username = request.POST.get('username', "").strip()
        password = request.POST.get('password', "").strip()
        if username and password:
            user_obj = authenticate(username=username, password=password)
            login(request, user_obj)

            return redirect(reverse('django_app:', args=()))
        else:
            raise Exception("данные не совпадают!")
    context = {}

    return render(request, "django_app/user_login.html", context)


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def logout_f(request):
    logout(request)
    return redirect(reverse("django_app:login", args=()))


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def create(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")

        django_models.PostModel.objects.create(
            author=request.user,
            title=title,
            description=description,
            is_completed=False,
        )

        return redirect(reverse("django_app:read_list", args=()))
    context = {}

    return render(request, "django_app/post_create.html", context)


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def read(request, post_id=None):
    post = django_utils.caching(
        LocMemCache, f"read django_models.PostModel.objects.get(id={post_id})", 2,
        lambda: django_models.PostModel.objects.get(id=post_id)
    )

    # _rating = django_models.PostRatingModel.objects.filter(post=post)
    # _rating_dislikes = _rating.filter(is_like=False).count()
    # _rating_likes = _rating.count() - _rating_dislikes
    #
    # _my_status = _rating.filter(user=request.user)
    # if _my_status.count() < 1:
    #     _my_status = 0
    # else:
    #     _my_status = 1 if _my_status[0].is_like is True else -1

    # context = {"post": post, "dislikes": _rating_dislikes, "likes": _rating_likes, "status": _my_status}

    # comments = django_models.PostCommentModel.objects.filter(post=post)
    # context = {"post": post, "comments": comments}

    # count = django_models.PostCommentModel.objects.filter(post=post).count()
    # context = {"post": post, "count": count}

    context = {"post": post}

    return render(request, "django_app/post_detail.html", context)


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def rating_like(request, post_id=None):
    post = django_models.PostModel.objects.get(id=post_id)
    user = request.user

    try:
        _rating = django_models.PostRatingModel.objects.get(post=post, user=user)
        like = _rating
        if like.is_like is True:
            like.delete()  # todo ЕСЛИ В БАЗЕ УЖЕ СТОИТ ЛАЙК
        else:
            like.is_like = True
            like.save()  # todo ЕСЛИ В БАЗЕ УЖЕ СТОИТ ДИЗЛАЙК
    except Exception as error:
        django_models.PostRatingModel.objects.create(
            user=user,
            post=post,
            is_like=True,
        )  # todo ЕСЛИ В БАЗЕ НЕТУ ОТМЕТКИ

    return redirect(reverse("django_app:read", args=(post_id,)))


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def rating_dislike(request, post_id=None):
    post = django_models.PostModel.objects.get(id=post_id)
    user = request.user

    _rating = django_models.PostRatingModel.objects.filter(post=post, user=user)
    if _rating.count() < 1:
        django_models.PostRatingModel.objects.create(
            user=user,
            post=post,
            is_like=False,
        )  # todo ЕСЛИ В БАЗЕ НЕТУ ОТМЕТКИ
    else:
        like = _rating[0]
        if like.is_like is True:
            like.is_like = False
            like.save()  # todo ЕСЛИ В БАЗЕ УЖЕ СТОИТ ЛАЙК
        else:
            like.delete()  # todo ЕСЛИ В БАЗЕ УЖЕ СТОИТ ДИЗЛАЙК

    return redirect(reverse("django_app:read", args=(post_id,)))


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def create_comment(request, post_id=None):
    django_models.PostCommentModel.objects.create(
        user=request.user,
        post=django_models.PostModel.objects.get(id=post_id),
        message=request.POST.get("message", ""),
    )

    return redirect(reverse("django_app:read", args=(post_id,)))


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def read_list(request):
    post_list = django_utils.caching(
        LocMemCache, f"read_list django_models.PostModel.objects.all()", 2,
        lambda: django_models.PostModel.objects.all()
    )

    is_detail_view = request.GET.get("is_detail_view", True)
    if is_detail_view == "False":
        is_detail_view = False
    elif is_detail_view == "True":
        is_detail_view = True

    page = django_utils.paginate(request=request, objects=post_list, num_page=4)
    context = {
        "page": page,
        "is_detail_view": is_detail_view
    }

    return render(request, "django_app/post_list.html", context)


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def update(request, post_id=None):
    if request.method == "POST":
        post = django_models.PostModel.objects.get(id=post_id)
        is_completed = request.POST.get("is_completed", "")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        if is_completed:
            if is_completed == "False":
                post.is_completed = False
            elif is_completed == "True":
                post.is_completed = True
        if title and title != post.title:
            post.title = title
        if description and description != post.description:
            post.description = description
        post.updated = timezone.now()
        post.save()

        return redirect(reverse("django_app:read_list", args=()))
    post = django_models.PostModel.objects.get(id=post_id)
    context = {
        "post": post
    }

    return render(request, "django_app/post_change.html", context)


@django_utils.logging_txt_decorator
@django_utils.login_required_decorator
def delete(request, post_id=None):
    django_models.PostModel.objects.get(id=post_id).delete()

    return redirect(reverse("django_app:read_list", args=()))
