from django import conf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.utils import timezone
from django.views.generic import View
from django.conf import settings
from . import models


def logging(controller_func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        request: WSGIRequest = args[0]
        print(request.META)
        # inits = models.LogModel.objects.filter(request.META["host_ip"], datetime__gte=)
        # if inits.count() > 30:
        #     raise Exception("подождите час!")

        models.LogModel.objects.create(
            user=request.user,
            method=request.method,
            status=0,
            url="",
            description="init"
        )
        try:
            response: HttpResponse = controller_func(*args, **kwargs)
            if settings.DEBUG_LOG:
                models.LogModel.objects.create(
                    user=request.user,
                    method=request.method,
                    status=200,
                    url="",
                    description="Response: " + str(response.content)
                )
            return response
        except Exception as error:
            models.LogModel.objects.create(
                user=request.user,
                method=request.method,
                status=500,
                url="",
                description="Error: " + str(error)
            )
            # return HttpResponse(status=500)
            context = {"detail": str(error)}
            if str(error).find("query does not exist"):
                context["extra"] = "Такого объекта не существует"
            return render(request, "components/error.html", context=context)

    return wrapper


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect(reverse('app_name_task_list:home', args=()))
    return render(request, 'pages/register.html', context={})


def sing_in(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  # Сохраняет текушую сессию в cookies browser
            return redirect(reverse('app_name_task_list:home', args=()))
        else:
            raise Exception("Логин или пароль не верны!")
    return render(request, 'pages/login.html')


def logout_(request):
    logout(request)
    return redirect(reverse('app_name_task_list:home', args=()))


def index(request):
    return HttpResponse("<h1>This is a Index Page</h1>")


def home(request):
    context = {
    }
    return render(request, 'pages/home.html', context)


def post(request):
    posts = models.Post.objects.all()
    return render(request, 'pages/Post_detail.html', context={'posts': posts})


@logging
def post_detail(request: WSGIRequest, pk: int):
    # get_object_or_404(models.Post, id=pk)
    post_ = models.Post.objects.get(id=pk)
    # post_comment = models.PostComment.objects.filter(article=post_)
    # post_like = len(models.PostLike.objects.filter(author=request.user, article=post_, status=True)) > 0
    context = {
        "post": post_,
        # "comments": post_comment,
        # "post_like": post_like
    }
    return render(request, 'app_task_list/pages/post_detail.html', context=context)


def create(request):
    if request.method == 'POST':
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        models.Task.objects.create(
            author=request.user,
            title=title,
            description=description,
            is_completed=False,
        )
        return redirect(reverse('app_name_task_list:read_list', args=()))
    context = {
    }
    return render(request, 'app_task_list/pages/task_create.html', context)


def read(request, task_id=None):
    task = models.Task.objects.get(id=task_id)
    context = {
        "task": task
    }
    return render(request, 'app_task_list/pages/task_detail.html', context)


def read_list(request):
    is_detail_view = request.GET.get("is_detail_view", True)
    if is_detail_view == "False":
        is_detail_view = False
    elif is_detail_view == "True":
        is_detail_view = True
    task_list = models.Task.objects.all()

    def paginate(objects, num_page):
        paginator = Paginator(objects, num_page)
        pages = request.GET.get('page')
        try:
            local_page = paginator.page(pages)
        except PageNotAnInteger:
            local_page = paginator.page(1)
        except EmptyPage:
            local_page = paginator.page(paginator.num_pages)
        return local_page

    page = paginate(objects=task_list, num_page=4)
    context = {
        "page": page,
        "is_detail_view": is_detail_view
    }
    return render(request, 'app_task_list/pages/task_list.html', context)


def update(request, task_id=None):
    if request.method == 'POST':
        task = models.Task.objects.get(id=task_id)
        is_completed = request.POST.get("is_completed", "")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        if is_completed:
            if is_completed == "False":
                task.is_completed = False
            elif is_completed == "True":
                task.is_completed = True
        if title and title != task.title:
            task.title = title
        if description and description != task.description:
            task.description = description
        task.updated = timezone.now()
        task.save()
        return redirect(reverse('app_name_task_list:read_list', args=()))
    task = models.Task.objects.get(id=task_id)
    context = {
        "task": task
    }
    return render(request, 'app_task_list/pages/task_change.html', context)


def delete(request, task_id=None):
    # models.Task.objects.get(id=task_id).delete()
    task = models.Task.objects.get(id=task_id)
    if task.author == request.user:
        task.delete()
    else:
        pass  # TODO Logging invalid action

    return redirect(reverse('app_name_task_list:read_list', args=()))


def post_ph(request, post_id=None):
    print(post_id)
    post_new = models.Post.objects.get(id=post_id)
    comment_new = models.PostComment.objects.filter(article=post_new)
    print(comment_new)
    context = {
        "post": post_new,
        'comments': comment_new
    }
    return render(request, 'app_task_list/pages/post_detail.html', context)


@logging
def post_comment_create(request, pk):
    post_obj = models.Post.objects.get(id=pk)
    if post_obj is not None:
        models.PostComment.objects.create(
            article=post_obj,
            author=request.user,
            description=request.POST.get("description", ""),
        )
    return redirect(reverse('app_name_task_list:post_detail', args=(pk,)))


@logging
def post_like(request, pk):
    post_obj = models.Post.objects.get(id=pk)
    print(post_obj)
    try:
        like_obj = models.PostLike.objects.get(article=post_obj, author=request.user)
    except Exception as error:
        like_obj = models.PostLike.objects.create(article=post_obj, author=request.user, status=False)

    like_obj.status = not like_obj.status
    like_obj.save()

    return redirect(reverse('app_name_task_list:post_detail', args=(pk,)))


@logging
def post_comment_delete(request, comment_pk):
    comment_obj = models.PostComment.objects.get(id=comment_pk)
    post_id = comment_obj.article.id
    comment_obj.delete()
    return redirect(reverse('app_name_task_list:post_detail', args=(post_id,)))


# TODO ####################################
def todo_list1(request):
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/todos/").json()

    # 0,1      15.0                                                3.0 (check qwadro 2.5) 15.0
    # rust (postgresql - index + ssd + nosql + ramdisk, redis) vs python (postgresql, redis) (30x)

    # 1 вставки кода из другого языка программирования (C++, Rust, Go/ Cython)
    # https://habr.com/ru/company/skillfactory/blog/718894/

    # 2 добавление типизации (pypy, mypy)
    # 3 использовать встроенные функции на C (itertools, filter, reduce, )

    def return_q(n):
        return n ** 2

    def check_odd(n):
        return n % 2 == 0

    def start():
        counter = 1
        for idx, elem in enumerate([1, 2, 3, 4], 1):
            counter += 1

    min_val = 0
    min_val = min([1, 2, 3, 4])
    for i in [1, 2, 3, 4]:
        if i < min_val:
            min_val = i

    list1 = range(1, 10000)
    # res = map(return_q, list1)
    res = filter(lambda n: n % 2 == 0, list1)
    print(tuple(res))

    return render(request=request, template_name="app_task_list/pages/todo_list1.html",
                  context={"success": {"data": response}})


class TodoList2(View):  # CreateView, LoginRequiredMixin
    # ftndfntdfg
    def get(self, request):
        # if request.user.is_auth:
        #     return redirect(reverse("login"))

        response = models.LogModel.objects.filter(status__gte=1)  # todo > 299
        return render(request=request, template_name="app_task_list/pages/todo_list1.html",
                      context={"success": {"data": response}})

    def post(self, request):
        # if request.user.is_auth:
        #     return redirect(reverse("login"))

        response = models.LogModel.objects.filter(status__gte=1)  # todo > 299
        return render(request=request, template_name="app_task_list/pages/todo_list1.html",
                      context={"success": {"data": response}})

# TODO ####################################
